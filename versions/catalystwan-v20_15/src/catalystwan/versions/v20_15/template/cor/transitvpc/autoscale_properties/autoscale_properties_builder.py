# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class AutoscalePropertiesBuilder:
    """
    Builds and executes requests for operations under /template/cor/transitvpc/autoscale-properties
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def update_transit_vpc_autoscale_properties(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Update transit VPC autoscale properties

        :param payload: VPC
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "updateTransitVpcAutoscaleProperties")
        return self._request_adapter.request(
            "PUT", "/dataservice/template/cor/transitvpc/autoscale-properties", payload=payload, **kw
        )
