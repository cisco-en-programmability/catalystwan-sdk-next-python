# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import List, Optional

from catalystwan.abc import RequestAdapterInterface

from .models import EventReadoutsResponsePayloadData


class EventReadoutByTracesBuilder:
    """
    Builds and executes requests for operations under /stream/device/nwpi/eventReadoutByTraces
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_event_readout_by_traces(
        self,
        trace_id: List[int],
        entry_time: List[int],
        vpn: Optional[str] = None,
        user_name: Optional[str] = None,
        **kw,
    ) -> EventReadoutsResponsePayloadData:
        """
        Get event Readout By Traces

        :param trace_id: traceId
        :param entry_time: entry_time
        :param vpn: vpn
        :param user_name: userName
        :returns: EventReadoutsResponsePayloadData
        """
        logging.warning("Operation: %s is deprecated", "getEventReadoutByTraces")
        params = {
            "trace_id": trace_id,
            "entry_time": entry_time,
            "vpn": vpn,
            "userName": user_name,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/stream/device/nwpi/eventReadoutByTraces",
            return_type=EventReadoutsResponsePayloadData,
            params=params,
            **kw,
        )
