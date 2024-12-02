# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class DetachcloudxBuilder:
    """
    Builds and executes requests for operations under /template/device/config/detachcloudx
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def detach_sites(self):
        class detach_sites_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> str:
                """
                Disable enabled gateways, clients, dias


                Note: In a multitenant vManage system, this API is only available in the Provider view.

                :param payload: CloudX config
                :returns: str
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/template/device/config/detachcloudx",
                    return_type=str,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return detach_sites_(self._request_adapter)
