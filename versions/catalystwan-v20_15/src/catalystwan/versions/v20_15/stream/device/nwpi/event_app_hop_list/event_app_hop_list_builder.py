# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import List, Optional

from catalystwan.abc import RequestAdapterInterface

from .models import EventAppHopListResponsePayloadInner


class EventAppHopListBuilder:
    """
    Builds and executes requests for operations under /stream/device/nwpi/eventAppHopList
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_event_app_hop_list(
        self,
        trace_id: int,
        timestamp: int,
        state: Optional[str] = None,
        version: Optional[str] = None,
        server_side_key: Optional[str] = None,
        client_side_key: Optional[str] = None,
        vpn: Optional[str] = None,
        **kw,
    ) -> List[EventAppHopListResponsePayloadInner]:
        """
        Get Trace Application and HopList for NWPI.

        :param trace_id: Trace id
        :param timestamp: Timestamp
        :param state: State
        :param version: Version
        :param server_side_key: Server side key
        :param client_side_key: Client side key
        :param vpn: Vpn
        :returns: List[EventAppHopListResponsePayloadInner]
        """
        logging.warning("Operation: %s is deprecated", "getEventAppHopList")
        params = {
            "traceId": trace_id,
            "timestamp": timestamp,
            "state": state,
            "version": version,
            "serverSideKey": server_side_key,
            "clientSideKey": client_side_key,
            "vpn": vpn,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/stream/device/nwpi/eventAppHopList",
            return_type=List[EventAppHopListResponsePayloadInner],
            params=params,
            **kw,
        )
