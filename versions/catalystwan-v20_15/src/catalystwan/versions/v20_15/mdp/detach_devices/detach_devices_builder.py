# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class DetachDevicesBuilder:
    """
    Builds and executes requests for operations under /mdp/detachDevices
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def detach_devices(self, nms_id: str, payload: Optional[Any] = None, **kw) -> Any:
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
            "POST", "/dataservice/mdp/detachDevices/{nmsId}", params=params, payload=payload, **kw
        )
