from __future__ import annotations

import logging
from copy import copy
from dataclasses import Field, dataclass, field, fields, is_dataclass
from string import Formatter
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar, Union, cast

from catalystwan.abc import RequestAdapterInterface, ResponseInterface, SessionInterface
from catalystwan.abc.types import HTTP_METHOD, JSON
from catalystwan.core.exceptions import CatalystwanResponseTypeError
from catalystwan.core.models.deserialize import deserialize
from catalystwan.core.models.serialize import serialize
from catalystwan.core.types import DataclassInstance, get_alias
from typing_extensions import get_args, get_origin

DataclassType = TypeVar("DataclassType", bound=DataclassInstance)
ReturnType = TypeVar("ReturnType")
Payload = TypeVar("Payload")


@dataclass
class ResponseDataPath:
    data_key: str
    required_keys: List[str] = field(default_factory=list)

    def is_data_available(self, data: Dict[str, Any]) -> bool:
        keys = self.required_keys + [self.data_key]
        return all(key in data for key in keys)

    def get_data(self, data: Dict[str, Any]) -> JSON:
        return data[self.data_key]


class RequestAdapter(RequestAdapterInterface):
    known_data_paths: List[ResponseDataPath] = [
        ResponseDataPath(data_key="data", required_keys=["header"]),
        ResponseDataPath(data_key="devices", required_keys=["header"]),
    ]

    def __init__(self, session: SessionInterface, logger: Optional[logging.Logger] = None):
        self.session = session
        self.logger = logger or logging.getLogger(__name__)

    def request(
        self,
        method: HTTP_METHOD,
        url: str,
        payload: Union[Payload, JSON] = None,
        params: Optional[dict] = None,
        return_type: Optional[Type[ReturnType]] = None,
        headers: Optional[dict] = None,
        **kwargs,
    ) -> Union[ReturnType, JSON, bytes, None]:
        if params:
            path_keys = [
                field_name
                for _, field_name, _, _ in Formatter().parse(url)
                if field_name is not None
            ]
            url = url.format_map({path_key: params.pop(path_key) for path_key in path_keys})
        if is_dataclass(payload):
            payload = serialize(cast(DataclassInstance, payload), to_json=True)
        response = self.session.request(
            method=method,
            url=url,
            json=payload,
            params=params,
            headers=headers,
            **kwargs,
        )

        content = self.__get_content(response)
        return self.__prepare_return_type(return_type, content)

    def __prepare_return_type(
        self, return_type: Optional[Type[ReturnType]], content: Union[JSON, str, bytes, None]
    ) -> Union[ReturnType, JSON, bytes, None]:
        if is_dataclass(return_type):
            return cast(
                ReturnType, self.__get_dataclass(return_type=return_type, model_payload=content)
            )
        elif get_origin(return_type) is list and type(content) is list:
            return [self.__parse_list(get_args(return_type)[0], value) for value in content]
        else:
            if type(content) is not return_type and return_type is not None:
                self.logger.warning(
                    f"Server returned unexpected data. Expected: {return_type}, received {type(content)}"
                )
            return content

    def __get_content(self, response: ResponseInterface) -> Union[JSON, str, bytes, None]:
        content_type: str = response.headers.get("content-type", "")
        if not content_type:
            return None
        if content_type == "application/json":
            return self.__extract_json_data(response.json())
        if content_type.startswith("text"):
            return response.text
        else:
            return response.content

    def __parse_list(
        self, arg_type: Type[ReturnType], values: Union[JSON]
    ) -> Union[ReturnType, JSON]:
        if is_dataclass(arg_type):
            model_payload = self.__extract_json_data(values, fields=fields(arg_type))
            return cast(
                ReturnType, self.__get_dataclass(return_type=arg_type, model_payload=model_payload)
            )
        elif get_origin(arg_type) is list:
            if not isinstance(values, list):
                raise CatalystwanResponseTypeError(
                    f"Expected type: list. Type received: {type(values)}"
                )
            return [self.__parse_list(get_args(arg_type)[0], value) for value in values]
        else:
            return values

    def __extract_json_data(self, data: JSON, fields: Optional[Tuple[Field, ...]] = None) -> JSON:
        if not isinstance(data, dict):
            return data
        # If we expect a model, see if necessary data is on the top-level of the json
        if fields is not None:
            field_names = [get_alias(field.metadata.get("alias", field.name)) for field in fields]
        else:
            field_names = []
        if field_names and all(key in data for key in field_names):
            return data
        for known_data_path in self.known_data_paths:
            if known_data_path.is_data_available(data):
                return known_data_path.get_data(data)
        return data

    def __get_dataclass(
        self, return_type: Type[DataclassType], model_payload: Union[JSON, str, bytes, None]
    ) -> DataclassType:
        if not isinstance(model_payload, dict):
            raise CatalystwanResponseTypeError(
                f"Expected data for {return_type} model. Received data of type {type(model_payload)} instead."
            )

        return deserialize(return_type, **model_payload)

    def __copy__(self) -> RequestAdapter:
        return RequestAdapter(session=copy(self.session), logger=self.logger)
