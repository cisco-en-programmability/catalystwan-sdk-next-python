# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from .models import VedgeCheckResponse


class VedgedetectionBuilder:
    """
    Builds and executes requests for operations under /system/device/vedgedetection
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def checkv_edge_device_presence(self, **kw) -> VedgeCheckResponse:
        """
        Check for Vedge Device Presence

        :returns: VedgeCheckResponse
        """
        return self._request_adapter.request(
            "GET", "/dataservice/system/device/vedgedetection", return_type=VedgeCheckResponse, **kw
        )
