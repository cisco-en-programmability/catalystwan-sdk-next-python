# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class TunnelpathBuilder:
    """
    Builds and executes requests for operations under /device/tools/tunnelpath
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def tunnel_path(self):
        class tunnel_path_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, device_ip: str, payload: Optional[Any] = None, **kw):
                """
                TunnelPath

                :param device_ip: Device IP
                :param payload: TunnelPath parameter
                :returns: None
                """
                params = {
                    "deviceIP": device_ip,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/device/tools/tunnelpath/{deviceIP}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return tunnel_path_(self._request_adapter)
