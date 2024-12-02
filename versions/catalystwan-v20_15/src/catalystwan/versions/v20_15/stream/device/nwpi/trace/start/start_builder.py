# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface
from .models import NwpiTraceStartRespPayload
from .models import NwpiTraceStartReqPayload


class StartBuilder:
    """
    Builds and executes requests for operations under /stream/device/nwpi/trace/start
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def trace_start(self):
        class trace_start_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
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

            def create_payload(self, *args, **kwargs) -> NwpiTraceStartReqPayload:
                return NwpiTraceStartReqPayload(*args, **kwargs)

            @property
            def payload_model(self) -> Type[NwpiTraceStartReqPayload]:
                return NwpiTraceStartReqPayload

        return trace_start_(self._request_adapter)
