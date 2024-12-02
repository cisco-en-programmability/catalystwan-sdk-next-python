# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import List

from catalystwan.abc import RequestAdapterInterface

from .models import TraceFinFlowTimeRangeResponsePayloadInner


class TraceFinFlowTimeRangeBuilder:
    """
    Builds and executes requests for operations under /stream/device/nwpi/traceFinFlowTimeRange
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_fin_flow_time_range(
        self, trace_id: int, timestamp: int, state: str, **kw
    ) -> List[TraceFinFlowTimeRangeResponsePayloadInner]:
        """
        Retrieve Fin Flow time range

        :param trace_id: Trace id
        :param timestamp: Timestamp
        :param state: State
        :returns: List[TraceFinFlowTimeRangeResponsePayloadInner]
        """
        logging.warning("Operation: %s is deprecated", "getFinFlowTimeRange")
        params = {
            "traceId": trace_id,
            "timestamp": timestamp,
            "state": state,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/stream/device/nwpi/traceFinFlowTimeRange",
            return_type=List[TraceFinFlowTimeRangeResponsePayloadInner],
            params=params,
            **kw,
        )
