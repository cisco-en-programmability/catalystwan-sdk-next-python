# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import ImportTraceRequest, ImportTraceResponse


class ImportTraceBuilder:
    """
    Builds and executes requests for operations under /stream/device/nwpi/importTrace
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def import_trace(self):
        class import_trace_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[ImportTraceRequest] = None, new_trace_name: Optional[str] = None, **kw
            ) -> ImportTraceResponse:
                """
                Import Trace

                :param new_trace_name: New trace name
                :param payload: Trace Data File
                :returns: ImportTraceResponse
                """
                params = {
                    "newTraceName": new_trace_name,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/stream/device/nwpi/importTrace",
                    return_type=ImportTraceResponse,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> ImportTraceRequest:
                return ImportTraceRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[ImportTraceRequest]:
                return ImportTraceRequest

        return import_trace_(self._request_adapter)
