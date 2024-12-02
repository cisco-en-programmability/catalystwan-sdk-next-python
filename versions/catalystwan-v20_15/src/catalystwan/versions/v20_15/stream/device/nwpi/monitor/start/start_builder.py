# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface
import logging
from .models import NwpiMonitorRespPayload
from .models import NwpiMonitorReqPayload


class StartBuilder:
    """
    Builds and executes requests for operations under /stream/device/nwpi/monitor/start
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def monitor_start(self):
        class monitor_start_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[NwpiMonitorReqPayload] = None, **kw
            ) -> NwpiMonitorRespPayload:
                """
                CXP Monitor Action - Start

                :param payload: Payload
                :returns: NwpiMonitorRespPayload
                """
                logging.warning("Operation: %s is deprecated", "monitorStart")
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/stream/device/nwpi/monitor/start",
                    return_type=NwpiMonitorRespPayload,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> NwpiMonitorReqPayload:
                return NwpiMonitorReqPayload(*args, **kwargs)

            @property
            def payload_model(self) -> Type[NwpiMonitorReqPayload]:
                return NwpiMonitorReqPayload

        return monitor_start_(self._request_adapter)
