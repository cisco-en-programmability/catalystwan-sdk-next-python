# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface
import logging


class WaniBuilder:
    """
    Builds and executes requests for operations under /settings/configuration/wani
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_wani_configuration(self, **kw) -> Any:
        """
        Retrieve wani configuration value

        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "getWaniConfiguration")
        return self._request_adapter.request(
            "GET", "/dataservice/settings/configuration/wani", **kw
        )

    @property
    def edit_wani_configuration(self):
        class edit_wani_configuration_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[str] = None, **kw) -> Any:
                """
                Update wani configuration setting

                :param payload: Payload
                :returns: Any
                """
                logging.warning("Operation: %s is deprecated", "editWaniConfiguration")
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/settings/configuration/wani",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return edit_wani_configuration_(self._request_adapter)

    @property
    def new_wani_configuration(self):
        class new_wani_configuration_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[str] = None, **kw) -> str:
                """
                Add new wani configuration

                :param payload: Payload
                :returns: str
                """
                logging.warning("Operation: %s is deprecated", "newWaniConfiguration")
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/settings/configuration/wani",
                    return_type=str,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return new_wani_configuration_(self._request_adapter)
