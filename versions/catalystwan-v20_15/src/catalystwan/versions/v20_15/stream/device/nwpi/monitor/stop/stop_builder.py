# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import NwpiMonitorReqPayload, NwpiMonitorRespPayload


class StopBuilder:
    """
    Builds and executes requests for operations under /stream/device/nwpi/monitor/stop
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def monitor_stop(self):
        class monitor_stop_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[NwpiMonitorReqPayload] = None, **kw
            ) -> NwpiMonitorRespPayload:
                """
                CXP Monitor Action - Stop

                :param payload: Payload
                :returns: NwpiMonitorRespPayload
                """
                logging.warning("Operation: %s is deprecated", "monitorStop")
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/stream/device/nwpi/monitor/stop",
                    return_type=NwpiMonitorRespPayload,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> NwpiMonitorReqPayload:
                return NwpiMonitorReqPayload(*args, **kwargs)

            @property
            def payload_model(self) -> Type[NwpiMonitorReqPayload]:
                return NwpiMonitorReqPayload

        return monitor_stop_(self._request_adapter)
