# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from .models import SgtResponse


class SgtBuilder:
    """
    Builds and executes requests for operations under /template/policy/ise/identity/sgt
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def sgts(self, **kw) -> SgtResponse:
        """
        Get trustsec Scalable Group Tags

        :returns: SgtResponse
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/template/policy/ise/identity/sgt",
            return_type=SgtResponse,
            **kw,
        )
