# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging

from catalystwan.abc import RequestAdapterInterface

from .models import NwpitraceFlowRespPayload


class TraceFlowBuilder:
    """
    Builds and executes requests for operations under /stream/device/nwpi/traceFlow
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_trace_flow(
        self, trace_id: int, timestamp: int, state: str, **kw
    ) -> NwpitraceFlowRespPayload:
        """
        getTraceFlow

        :param trace_id: trace id
        :param timestamp: start time
        :param state: trace state
        :returns: NwpitraceFlowRespPayload
        """
        logging.warning("Operation: %s is deprecated", "getTraceFlow")
        params = {
            "traceId": trace_id,
            "timestamp": timestamp,
            "state": state,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/stream/device/nwpi/traceFlow",
            return_type=NwpitraceFlowRespPayload,
            params=params,
            **kw,
        )
