# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Any
from catalystwan.abc import RequestAdapterInterface
import logging


class EdgeBuilder:
    """
    Builds and executes requests for operations under /multicloud/widget/edge
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_all_edge_widgets(self, **kw) -> Any:
        """
        Get All Interconnect Edge widgets

        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "getAllEdgeWidgets")
        return self._request_adapter.request(
            "GET", "/dataservice/multicloud/widget/edge", **kw
        )

    def get_edge_widget(self, edge_type: str, **kw) -> Any:
        """
        Get Interconnect Edge widget by edge type

        :param edge_type: Edge type
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "getEdgeWidget")
        params = {
            "edgeType": edge_type,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/multicloud/widget/edge/{edgeType}", params=params, **kw
        )
