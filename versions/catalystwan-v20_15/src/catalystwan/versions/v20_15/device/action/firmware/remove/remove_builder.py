# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class RemoveBuilder:
    """
    Builds and executes requests for operations under /device/action/firmware/remove
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def remove_firmware_image(self, payload: Optional[str] = None, **kw):
        """
        Remove firmware on device

        :param payload: Payload
        :returns: None
        """
        logging.warning("Operation: %s is deprecated", "removeFirmwareImage")
        return self._request_adapter.request(
            "POST", "/dataservice/device/action/firmware/remove", payload=payload, **kw
        )
