# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import List
from catalystwan.abc import RequestAdapterInterface
import logging
from .models import DeviceBlistResponsePayloadInner


class GetBuilder:
    """
    Builds and executes requests for operations under /stream/device/nwpi/device/blist/get
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_device_b_list(self, **kw) -> List[DeviceBlistResponsePayloadInner]:
        """
        Get Device BlackList for NWPI.

        :returns: List[DeviceBlistResponsePayloadInner]
        """
        logging.warning("Operation: %s is deprecated", "getDeviceBList")
        return self._request_adapter.request(
            "GET",
            "/dataservice/stream/device/nwpi/device/blist/get",
            return_type=List[DeviceBlistResponsePayloadInner],
            **kw,
        )
