# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import List, Any
from catalystwan.abc import RequestAdapterInterface


class LocaldcBuilder:
    """
    Builds and executes requests for operations under /disasterrecovery/localdc
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_local_data_center_state(self, **kw) -> List[Any]:
        """
        Get local data center details

        :returns: List[Any]
        """
        return self._request_adapter.request(
            "GET", "/dataservice/disasterrecovery/localdc", return_type=List[Any], **kw
        )
