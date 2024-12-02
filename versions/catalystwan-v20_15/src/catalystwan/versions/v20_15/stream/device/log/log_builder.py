# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface
from .models import Uuid

if TYPE_CHECKING:
    from .disable.disable_builder import DisableBuilder
    from .download.download_builder import DownloadBuilder
    from .renew.renew_builder import RenewBuilder
    from .search.search_builder import SearchBuilder
    from .sessions.sessions_builder import SessionsBuilder
    from .type_.type_builder import TypeBuilder


class LogBuilder:
    """
    Builds and executes requests for operations under /stream/device/log
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_session_info_log(self):
        class get_session_info_log_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[str] = None, **kw):
                """
                Get session info log

                :param payload: Payload
                :returns: None
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/stream/device/log", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return get_session_info_log_(self._request_adapter)

    @property
    def stream_log(self):
        class stream_log_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                log_type: str,
                device_uuid: str,
                session_id: str,
                payload: Optional[str] = None,
                **kw,
            ):
                """
                Stream log

                :param log_type: Log type
                :param device_uuid: Device uuid
                :param session_id: Session Id
                :param payload: Payload
                :returns: None
                """
                params = {
                    "logType": log_type,
                    "deviceUUID": device_uuid,
                    "sessionId": session_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/stream/device/log/{logType}/{deviceUUID}/{sessionId}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return stream_log_(self._request_adapter)

    def get_device_log(self, session_id: Uuid, log_id: Optional[int] = -1, **kw):
        """
        Get device log

        :param session_id: Session id
        :param log_id: Log id
        :returns: None
        """
        params = {
            "sessionId": session_id,
            "logId": log_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/stream/device/log/{sessionId}", params=params, **kw
        )

    @property
    def disable(self) -> DisableBuilder:
        """
        The disable property
        """
        from .disable.disable_builder import DisableBuilder

        return DisableBuilder(self._request_adapter)

    @property
    def download(self) -> DownloadBuilder:
        """
        The download property
        """
        from .download.download_builder import DownloadBuilder

        return DownloadBuilder(self._request_adapter)

    @property
    def renew(self) -> RenewBuilder:
        """
        The renew property
        """
        from .renew.renew_builder import RenewBuilder

        return RenewBuilder(self._request_adapter)

    @property
    def search(self) -> SearchBuilder:
        """
        The search property
        """
        from .search.search_builder import SearchBuilder

        return SearchBuilder(self._request_adapter)

    @property
    def sessions(self) -> SessionsBuilder:
        """
        The sessions property
        """
        from .sessions.sessions_builder import SessionsBuilder

        return SessionsBuilder(self._request_adapter)

    @property
    def type_(self) -> TypeBuilder:
        """
        The type property
        """
        from .type_.type_builder import TypeBuilder

        return TypeBuilder(self._request_adapter)
