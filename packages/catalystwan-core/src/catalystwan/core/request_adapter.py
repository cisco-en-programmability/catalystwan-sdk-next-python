from copy import copy
from dataclasses import Field, dataclass, field, fields, is_dataclass
from string import Formatter
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

from catalystwan.abc import RequestAdapterInterface, ResponseInterface, SessionInterface
from catalystwan.abc.types import HTTP_METHOD, JSON
from typing_extensions import Self, get_args, get_origin

from catalystwan.core.models.deserialize import deserialize
from catalystwan.core.models.serialize import serialize
from catalystwan.core.types import get_alias

T = TypeVar("T")


@dataclass
class ResponseDataPath:
    data_key: str
    required_keys: List[str] = field(default_factory=list)

    def is_data_available(self, data: Dict[str, Any]) -> bool:
        keys = self.required_keys + [self.data_key]
        return all(key in data for key in keys)

    def get_data(self, data: Dict[str, Any]) -> Any:
        return data[self.data_key]


class RequestAdapter(RequestAdapterInterface):
    known_data_paths: List[ResponseDataPath] = [
        ResponseDataPath(data_key="data", required_keys=["header"]),
        ResponseDataPath(data_key="devices", required_keys=["header"]),
    ]

    def __init__(self, session: SessionInterface):
        self.session = session

    def request(
        self,
        method: HTTP_METHOD,
        url: str,
        payload: Optional[JSON] = None,
        params: Optional[dict] = None,
        return_type: Optional[Type[T]] = None,
        headers: Optional[dict] = None,
        *args,
        **kwargs,
    ) -> Union[T, Any]:
        if params:
            path_keys = [
                field_name
                for _, field_name, _, _ in Formatter().parse(url)
                if field_name is not None
            ]
            url = url.format_map(
                {path_key: params.pop(path_key) for path_key in path_keys}
            )
        if is_dataclass(payload):
            payload = serialize(payload, to_json=True)
        response = self.session.request(
            method=method,
            url=url,
            json=payload,
            params=params,
            headers=headers,
            *args,
            **kwargs,
        )

        return self.__prepare_return_type(return_type, response)

    def get(
        self,
        url: str,
        payload: Optional[dict] = None,
        params: Optional[dict] = None,
        return_type: Optional[Type[T]] = None,
        headers: Optional[dict] = None,
        *args,
        **kwargs,
    ) -> Union[T, Any]:
        return self.request(
            method="GET",
            url=url,
            payload=payload,
            params=params,
            return_type=return_type,
            headers=headers,
            *args,
            **kwargs,
        )

    def put(
        self,
        url: str,
        payload: Optional[dict] = None,
        params: Optional[dict] = None,
        return_type: Optional[Type[T]] = None,
        headers: Optional[dict] = None,
        *args,
        **kwargs,
    ) -> Union[T, Any]:
        return self.request(
            method="PUT",
            url=url,
            payload=payload,
            params=params,
            return_type=return_type,
            headers=headers,
            *args,
            **kwargs,
        )

    def post(
        self,
        url: str,
        payload: Optional[dict] = None,
        params: Optional[dict] = None,
        return_type: Optional[Type[T]] = None,
        headers: Optional[dict] = None,
        *args,
        **kwargs,
    ) -> Union[T, Any]:
        return self.request(
            method="POST",
            url=url,
            payload=payload,
            params=params,
            return_type=return_type,
            headers=headers,
            *args,
            **kwargs,
        )

    def delete(
        self,
        url: str,
        payload: Optional[dict] = None,
        params: Optional[dict] = None,
        return_type: Optional[Type[T]] = None,
        headers: Optional[dict] = None,
        *args,
        **kwargs,
    ) -> Union[T, Any]:
        return self.request(
            method="DELETE",
            url=url,
            payload=payload,
            params=params,
            return_type=return_type,
            headers=headers,
            *args,
            **kwargs,
        )

    def __prepare_return_type(
        self, return_type: Optional[Type[T]], response: ResponseInterface
    ) -> Union[T, str, dict, bytes, None]:
        if return_type is None:
            return self.__get_return_type_from_content_type(response)
        elif return_type is dict:
            return self.__extract_json_data(response.json())
        elif return_type is str:
            return response.text
        elif return_type is bytes:
            return response.content
        elif is_dataclass(return_type):
            return deserialize(
                return_type,
                **self.__extract_json_data(response.json(), fields=fields(return_type)),
            )
        elif get_origin(return_type) is list:
            return [
                self.__parse_list(get_args(return_type)[0], value)
                for value in self.__extract_json_data(response.json())
            ]
        else:
            return None

    def __get_return_type_from_content_type(
        self, response: ResponseInterface
    ) -> Union[str, dict, bytes, None]:
        content_type: str = response.headers.get("content-type", "")
        if not content_type:
            return None
        if content_type == "application/json":
            return self.__extract_json_data(response.json())
        if content_type.startswith("text"):
            return response.text
        else:
            return response.content

    def __parse_list(self, arg_type: Type[T], values: Union[List[Any], dict, Any]) -> T:
        if get_origin(arg_type) is list:
            return [self.__parse_list(get_args(arg_type)[0], value) for value in values]
        elif is_dataclass(arg_type):
            return deserialize(arg_type, **values)
        else:
            return values

    def __extract_json_data(self, data: JSON, fields: Optional[List[Field]] = None):
        if not isinstance(data, dict):
            return data
        # If we expect a model, see if necessary data is on the top-level of the json
        if fields is not None:
            field_names = [
                get_alias(field.metadata.get("alias", field.name)) for field in fields
            ]
        else:
            field_names = []
        if field_names and all(key in data for key in field_names):
            return data
        for known_data_path in self.known_data_paths:
            if known_data_path.is_data_available(data):
                return known_data_path.get_data(data)
        return data

    def __copy__(self) -> Self:
        return RequestAdapter(session=copy(self.session))
