# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class WanedgeBuilder:
    """
    Builds and executes requests for operations under /sslproxy/certificate/wanedge
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def add_wan_edge(self):
        class add_wan_edge_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, device_id: str, payload: Optional[Any] = None, **kw):
                """
                Add SSL proxy wan edge

                :param device_id: Device Id
                :param payload: Cert state
                :returns: None
                """
                params = {
                    "deviceId": device_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/sslproxy/certificate/wanedge/{deviceId}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return add_wan_edge_(self._request_adapter)
