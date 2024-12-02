# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Type
from catalystwan.abc import RequestAdapterInterface
from .models import Taskid
from .models import TelemetryRequests


class TelemetryBuilder:
    """
    Builds and executes requests for operations under /multicloud/telemetry
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def telemetry(self):
        class telemetry_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: TelemetryRequests, **kw) -> Taskid:
                """
                Reports telemetry data

                :param payload: telemetry
                :returns: Taskid
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/multicloud/telemetry",
                    return_type=Taskid,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> TelemetryRequests:
                return TelemetryRequests(*args, **kwargs)

            @property
            def payload_model(self) -> Type[TelemetryRequests]:
                return TelemetryRequests

        return telemetry_(self._request_adapter)
