# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import (SpeedTestResponse, SpeedTestResult, SpeedTestResultResponse, SpeedTestSession,
                     SpeedTestStatusResponse, Uuid)

if TYPE_CHECKING:
    from .disable.disable_builder import DisableBuilder
    from .interface.interface_builder import InterfaceBuilder
    from .start.start_builder import StartBuilder
    from .status.status_builder import StatusBuilder
    from .stop.stop_builder import StopBuilder


class SpeedBuilder:
    """
    Builds and executes requests for operations under /stream/device/speed
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_session(self):
        class get_session_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: SpeedTestSession, **kw) -> SpeedTestResponse:
                """
                Get session

                :param payload: Payload
                :returns: SpeedTestResponse
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/stream/device/speed",
                    return_type=SpeedTestResponse,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> SpeedTestSession:
                return SpeedTestSession(*args, **kwargs)

            @property
            def payload_model(self) -> Type[SpeedTestSession]:
                return SpeedTestSession

        return get_session_(self._request_adapter)

    @property
    def save_speed_test_results(self):
        class save_speed_test_results_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                device_uuid: str,
                session_id: Uuid,
                payload: Optional[SpeedTestResult] = None,
                **kw,
            ) -> SpeedTestStatusResponse:
                """
                Save speed test results

                :param device_uuid: Device uuid
                :param session_id: sessionId
                :param payload: SpeedTestResult
                :returns: SpeedTestStatusResponse
                """
                params = {
                    "deviceUUID": device_uuid,
                    "sessionId": session_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/stream/device/speed/{deviceUUID}/{sessionId}",
                    return_type=SpeedTestStatusResponse,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> SpeedTestResult:
                return SpeedTestResult(*args, **kwargs)

            @property
            def payload_model(self) -> Type[SpeedTestResult]:
                return SpeedTestResult

        return save_speed_test_results_(self._request_adapter)

    def get_speed_test(
        self, session_id: Uuid, log_id: Optional[int] = 0, **kw
    ) -> SpeedTestResultResponse:
        """
        Get speed test

        :param session_id: sessionId
        :param log_id: Log id
        :returns: SpeedTestResultResponse
        """
        params = {
            "sessionId": session_id,
            "logId": log_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/stream/device/speed/{sessionId}",
            return_type=SpeedTestResultResponse,
            params=params,
            **kw,
        )

    @property
    def disable(self) -> DisableBuilder:
        """
        The disable property
        """
        from .disable.disable_builder import DisableBuilder

        return DisableBuilder(self._request_adapter)

    @property
    def interface(self) -> InterfaceBuilder:
        """
        The interface property
        """
        from .interface.interface_builder import InterfaceBuilder

        return InterfaceBuilder(self._request_adapter)

    @property
    def start(self) -> StartBuilder:
        """
        The start property
        """
        from .start.start_builder import StartBuilder

        return StartBuilder(self._request_adapter)

    @property
    def status(self) -> StatusBuilder:
        """
        The status property
        """
        from .status.status_builder import StatusBuilder

        return StatusBuilder(self._request_adapter)

    @property
    def stop(self) -> StopBuilder:
        """
        The stop property
        """
        from .stop.stop_builder import StopBuilder

        return StopBuilder(self._request_adapter)
