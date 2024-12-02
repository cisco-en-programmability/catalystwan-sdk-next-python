# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import InlineResponse200, LocalBackupInfo


class ExportBuilder:
    """
    Builds and executes requests for operations under /backup/export
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def export_backup(self):
        class export_backup_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[LocalBackupInfo] = None, **kw
            ) -> InlineResponse200:
                """
                Trigger a backup of configuration database and statstics database and store it in vManage

                :param payload: backup request information
                :returns: InlineResponse200
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/backup/export",
                    return_type=InlineResponse200,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> LocalBackupInfo:
                return LocalBackupInfo(*args, **kwargs)

            @property
            def payload_model(self) -> Type[LocalBackupInfo]:
                return LocalBackupInfo

        return export_backup_(self._request_adapter)
