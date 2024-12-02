# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class DetachDevicesBuilder:
    """
    Builds and executes requests for operations under /mdp/detachDevices
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def detach_devices(self):
        class detach_devices_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, nms_id: str, payload: Optional[Any] = None, **kw) -> Any:
                """
                Disconnect devices from mpd controller

                :param nms_id: Nms id
                :param payload: deviceList
                :returns: Any
                """
                params = {
                    "nmsId": nms_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/mdp/detachDevices/{nmsId}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return detach_devices_(self._request_adapter)
