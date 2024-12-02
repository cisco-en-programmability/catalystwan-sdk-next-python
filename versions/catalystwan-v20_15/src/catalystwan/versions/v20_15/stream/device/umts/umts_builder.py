# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import UmtsInput, UmtsSession

if TYPE_CHECKING:
    from .save.save_builder import SaveBuilder
    from .statistics.statistics_builder import StatisticsBuilder


class UmtsBuilder:
    """
    Builds and executes requests for operations under /stream/device/umts
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def enable_session(self):
        class enable_session_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[UmtsInput] = None, **kw
            ) -> List[UmtsSession]:
                """
                assign sessionId to client if there is no conflict ongoing sessions

                :param payload: Input query
                :returns: List[UmtsSession]
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/stream/device/umts",
                    return_type=List[UmtsSession],
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> UmtsInput:
                return UmtsInput(*args, **kwargs)

            @property
            def payload_model(self) -> Type[UmtsInput]:
                return UmtsInput

        return enable_session_(self._request_adapter)

    def update_umts_session_status(self, operation: str, session_id: str, **kw) -> Any:
        """
        start, stop,status,download or disable session

        :param operation: Operation
        :param session_id: Session id
        :returns: Any
        """
        params = {
            "operation": operation,
            "sessionId": session_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/stream/device/umts/{operation}/{sessionId}",
            params=params,
            **kw,
        )

    @property
    def save(self) -> SaveBuilder:
        """
        The save property
        """
        from .save.save_builder import SaveBuilder

        return SaveBuilder(self._request_adapter)

    @property
    def statistics(self) -> StatisticsBuilder:
        """
        The statistics property
        """
        from .statistics.statistics_builder import StatisticsBuilder

        return StatisticsBuilder(self._request_adapter)
