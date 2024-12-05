# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from .models import NwpiTraceHistoryRespPayload


class TraceHistoryBuilder:
    """
    Builds and executes requests for operations under /stream/device/nwpi/traceHistory
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_trace_history(self, trace_model: Optional[str] = None, **kw) -> NwpiTraceHistoryRespPayload:
        """
        Get historical traces

        :param trace_model: traceModel
        :returns: NwpiTraceHistoryRespPayload
        """
        params = {
            "traceModel": trace_model,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/stream/device/nwpi/traceHistory",
            return_type=NwpiTraceHistoryRespPayload,
            params=params,
            **kw,
        )
