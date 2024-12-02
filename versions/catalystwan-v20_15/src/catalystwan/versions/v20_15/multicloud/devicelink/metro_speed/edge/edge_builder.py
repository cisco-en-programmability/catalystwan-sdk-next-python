# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface
import logging


class EdgeBuilder:
    """
    Builds and executes requests for operations under /multicloud/devicelink/metroSpeed/edge
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_device_link_metro_speed(self):
        class get_device_link_metro_speed_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Get Device Link Metro Speed based on device link config

                :param payload: Device Link
                :returns: Any
                """
                logging.warning(
                    "Operation: %s is deprecated", "getDeviceLinkMetroSpeed"
                )
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/multicloud/devicelink/metroSpeed/edge",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return get_device_link_metro_speed_(self._request_adapter)
