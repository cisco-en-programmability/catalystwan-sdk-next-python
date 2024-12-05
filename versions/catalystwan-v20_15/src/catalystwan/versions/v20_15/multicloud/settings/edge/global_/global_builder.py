# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface

from .models import EdgeTypeParam


class GlobalBuilder:
    """
    Builds and executes requests for operations under /multicloud/settings/edge/global
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_edge_global_settings(self, edge_type: EdgeTypeParam, **kw) -> Any:
        """
        Get edge global settings

        :param edge_type: Edge type
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "getEdgeGlobalSettings")
        params = {
            "edgeType": edge_type,
        }
        return self._request_adapter.request("GET", "/dataservice/multicloud/settings/edge/global", params=params, **kw)

    def update_edge_global_settings(self, payload: Optional[Any] = None, **kw):
        """
        Update edge global settings for Edge provider

        :param payload: Global setting
        :returns: None
        """
        logging.warning("Operation: %s is deprecated", "updateEdgeGlobalSettings")
        return self._request_adapter.request(
            "PUT", "/dataservice/multicloud/settings/edge/global", payload=payload, **kw
        )

    def add_edge_global_settings(self, payload: Optional[Any] = None, **kw):
        """
        Add global settings for Edge provider

        :param payload: Global setting
        :returns: None
        """
        logging.warning("Operation: %s is deprecated", "addEdgeGlobalSettings")
        return self._request_adapter.request(
            "POST", "/dataservice/multicloud/settings/edge/global", payload=payload, **kw
        )
