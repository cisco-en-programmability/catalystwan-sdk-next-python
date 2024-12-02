# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class UnlockBuilder:
    """
    Builds and executes requests for operations under /system/device/{uuid}/unlock
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def unlock_device(self, uuid: str, payload: Optional[Any] = None, **kw):
        """
        Unlock device

        :param uuid: Device uuid
        :param payload: Device config
        :returns: None
        """
        params = {
            "uuid": uuid,
        }
        return self._request_adapter.request(
            "POST", "/dataservice/system/device/{uuid}/unlock", params=params, payload=payload, **kw
        )
