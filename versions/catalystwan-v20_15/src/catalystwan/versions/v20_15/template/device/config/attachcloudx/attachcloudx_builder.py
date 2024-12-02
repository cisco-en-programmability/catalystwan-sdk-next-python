# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class AttachcloudxBuilder:
    """
    Builds and executes requests for operations under /template/device/config/attachcloudx
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def edit_cloudx_config(self):
        class edit_cloudx_config_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> str:
                """
                Edit already enabled gateways, clients, dias


                Note: In a multitenant vManage system, this API is only available in the Provider view.

                :param payload: CloudX config
                :returns: str
                """
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/template/device/config/attachcloudx",
                    return_type=str,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return edit_cloudx_config_(self._request_adapter)

    @property
    def push_cloudx_config(self):
        class push_cloudx_config_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> str:
                """
                Enable gateways, clients, dias

                :param payload: CloudX config
                :returns: str
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/template/device/config/attachcloudx",
                    return_type=str,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return push_cloudx_config_(self._request_adapter)
