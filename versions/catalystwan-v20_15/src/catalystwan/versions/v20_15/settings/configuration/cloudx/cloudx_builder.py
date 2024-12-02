# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface
import logging


class CloudxBuilder:
    """
    Builds and executes requests for operations under /settings/configuration/cloudx
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_cloudx_configuration(self, **kw) -> Any:
        """
        Retrieve cloudx configuration value

        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "getCloudxConfiguration")
        return self._request_adapter.request(
            "GET", "/dataservice/settings/configuration/cloudx", **kw
        )

    @property
    def edit_cloudx_configuration(self):
        class edit_cloudx_configuration_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[str] = None, **kw) -> Any:
                """
                Update cloudx configuration setting

                :param payload: Payload
                :returns: Any
                """
                logging.warning(
                    "Operation: %s is deprecated", "editCloudxConfiguration"
                )
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/settings/configuration/cloudx",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return edit_cloudx_configuration_(self._request_adapter)

    @property
    def new_cloudx_configuration(self):
        class new_cloudx_configuration_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[str] = None, **kw) -> str:
                """
                Add new cloudx configuration

                :param payload: Payload
                :returns: str
                """
                logging.warning("Operation: %s is deprecated", "newCloudxConfiguration")
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/settings/configuration/cloudx",
                    return_type=str,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return new_cloudx_configuration_(self._request_adapter)
