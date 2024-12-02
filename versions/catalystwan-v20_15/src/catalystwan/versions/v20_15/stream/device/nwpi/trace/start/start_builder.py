# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import NwpiTraceStartReqPayload, NwpiTraceStartRespPayload


class StartBuilder:
    """
    Builds and executes requests for operations under /stream/device/nwpi/trace/start
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def trace_start(
        self, payload: Optional[NwpiTraceStartReqPayload] = None, **kw
    ) -> NwpiTraceStartRespPayload:
        """
        Trace Action - Start

        :param payload: Payload
        :returns: NwpiTraceStartRespPayload
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/stream/device/nwpi/trace/start",
            return_type=NwpiTraceStartRespPayload,
            payload=payload,
            **kw,
        )
