# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import List, Any
from catalystwan.abc import RequestAdapterInterface


class SequencesBuilder:
    """
    Builds and executes requests for operations under /partner/aci/policy/sequences
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_data_prefix_sequences(self, **kw) -> List[Any]:
        """
        Get data prefix sequence

        :returns: List[Any]
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/partner/aci/policy/sequences",
            return_type=List[Any],
            **kw,
        )
