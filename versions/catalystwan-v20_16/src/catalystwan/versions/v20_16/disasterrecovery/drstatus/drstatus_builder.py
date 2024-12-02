# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List

from catalystwan.abc import RequestAdapterInterface


class DrstatusBuilder:
    """
    Builds and executes requests for operations under /disasterrecovery/drstatus
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_disaster_recovery_status(self, **kw) -> List[Any]:
        """
        Disaster recovery status

        :returns: List[Any]
        """
        return self._request_adapter.request(
            "GET", "/dataservice/disasterrecovery/drstatus", return_type=List[Any], **kw
        )
