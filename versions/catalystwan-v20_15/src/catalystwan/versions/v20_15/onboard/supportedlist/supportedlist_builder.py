# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import List, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import SupportedResponse


class SupportedlistBuilder:
    """
    Builds and executes requests for operations under /onboard/supportedlist
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_supported_features(
        self, payload: Optional[List[str]] = None, **kw
    ) -> SupportedResponse:
        """
        Manual Onboard Supported Device features

        :param payload: Manual Onboard Supported Device
        :returns: SupportedResponse
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/onboard/supportedlist",
            return_type=SupportedResponse,
            payload=payload,
            **kw,
        )
