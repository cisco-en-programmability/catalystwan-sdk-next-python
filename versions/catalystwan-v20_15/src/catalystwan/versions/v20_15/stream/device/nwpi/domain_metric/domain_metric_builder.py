# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List
from catalystwan.abc import RequestAdapterInterface
import logging
from .models import DomainMetricResponsePayloadInner


class DomainMetricBuilder:
    """
    Builds and executes requests for operations under /stream/device/nwpi/domainMetric
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_domain_metric(
        self,
        trace_id: int,
        timestamp: int,
        domain: str,
        first_timestamp: int,
        last_timestamp: int,
        trace_model: Optional[str] = None,
        **kw,
    ) -> List[DomainMetricResponsePayloadInner]:
        """
        Get domain metric

        :param trace_id: Trace id
        :param timestamp: Timestamp
        :param domain: Domain
        :param first_timestamp: First timestamp
        :param last_timestamp: Last timestamp
        :param trace_model: Trace model
        :returns: List[DomainMetricResponsePayloadInner]
        """
        logging.warning("Operation: %s is deprecated", "getDomainMetric")
        params = {
            "traceId": trace_id,
            "timestamp": timestamp,
            "domain": domain,
            "firstTimestamp": first_timestamp,
            "lastTimestamp": last_timestamp,
            "traceModel": trace_model,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/stream/device/nwpi/domainMetric",
            return_type=List[DomainMetricResponsePayloadInner],
            params=params,
            **kw,
        )
