# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional

from catalystwan.abc import RequestAdapterInterface


class ClouddiscoveredappBuilder:
    """
    Builds and executes requests for operations under /template/policy/clouddiscoveredapp
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_cloud_discovered_apps(self, **kw) -> List[Any]:
        """
        Get all cloud discovered applications

        :returns: List[Any]
        """
        return self._request_adapter.request(
            "GET", "/dataservice/template/policy/clouddiscoveredapp", return_type=List[Any], **kw
        )

    def map_traffic_profiles(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Set SLA class for policy cloud discovered applications

        :param payload: App payload
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/template/policy/clouddiscoveredapp", payload=payload, **kw
        )
