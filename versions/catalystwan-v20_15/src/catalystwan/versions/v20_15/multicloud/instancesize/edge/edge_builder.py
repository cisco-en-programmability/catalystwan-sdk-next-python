# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface

from .models import EdgeTypeParam


class EdgeBuilder:
    """
    Builds and executes requests for operations under /multicloud/instancesize/edge
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_supported_edge_instance_size(self, edge_type: Optional[EdgeTypeParam] = "MEGAPORT", **kw) -> Any:
        """
        Get Edge provider supported size

        :param edge_type: Edge type
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "getSupportedEdgeInstanceSize")
        params = {
            "edgeType": edge_type,
        }
        return self._request_adapter.request("GET", "/dataservice/multicloud/instancesize/edge", params=params, **kw)
