# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List
from catalystwan.abc import RequestAdapterInterface
import logging
from .models import ConcurrentDomainDataResponsePayloadInner


class ConcurrentDomainDataBuilder:
    """
    Builds and executes requests for operations under /stream/device/nwpi/concurrentDomainData
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_concurrent_domain_data(
        self, trace_id: int, timestamp: int, query: Optional[str] = None, **kw
    ) -> List[ConcurrentDomainDataResponsePayloadInner]:
        """
        Get concurrent domain data for NWPI.

        :param trace_id: Trace id
        :param timestamp: Timestamp
        :param query: Query
        :returns: List[ConcurrentDomainDataResponsePayloadInner]
        """
        logging.warning("Operation: %s is deprecated", "getConcurrentDomainData")
        params = {
            "traceId": trace_id,
            "timestamp": timestamp,
            "query": query,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/stream/device/nwpi/concurrentDomainData",
            return_type=List[ConcurrentDomainDataResponsePayloadInner],
            params=params,
            **kw,
        )
