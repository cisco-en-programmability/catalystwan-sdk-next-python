# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List
from catalystwan.abc import RequestAdapterInterface
import logging
from .models import AggFlowResponsePayloadInner


class AggFlowBuilder:
    """
    Builds and executes requests for operations under /stream/device/nwpi/aggFlow
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_agg_flow(
        self,
        trace_id: int,
        timestamp: int,
        trace_state: str,
        query: Optional[str] = None,
        **kw,
    ) -> List[AggFlowResponsePayloadInner]:
        """
        Get aggregated flow data for NWPI.

        :param trace_id: Trace id
        :param timestamp: Timestamp
        :param trace_state: Trace state
        :param query: Query
        :returns: List[AggFlowResponsePayloadInner]
        """
        logging.warning("Operation: %s is deprecated", "getAggFlow")
        params = {
            "traceId": trace_id,
            "timestamp": timestamp,
            "traceState": trace_state,
            "query": query,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/stream/device/nwpi/aggFlow",
            return_type=List[AggFlowResponsePayloadInner],
            params=params,
            **kw,
        )
