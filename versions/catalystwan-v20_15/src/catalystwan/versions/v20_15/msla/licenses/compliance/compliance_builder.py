# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import List, Any
from catalystwan.abc import RequestAdapterInterface


class ComplianceBuilder:
    """
    Builds and executes requests for operations under /msla/licenses/compliance
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_licenses_compliance(self, **kw) -> List[Any]:
        """
        Retrieve list of devices and their subscription information

        :returns: List[Any]
        """
        return self._request_adapter.request(
            "GET", "/dataservice/msla/licenses/compliance", return_type=List[Any], **kw
        )
