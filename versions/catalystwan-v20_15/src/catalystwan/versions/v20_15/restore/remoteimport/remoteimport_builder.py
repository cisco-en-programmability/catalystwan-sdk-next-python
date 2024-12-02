# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class RemoteimportBuilder:
    """
    Builds and executes requests for operations under /restore/remoteimport
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def remote_import_backup(self):
        class remote_import_backup_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Remote import backup from a remote URL and import the data and apply it to the configuraion database

                :param payload: ImportBackupInfo Payload
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/restore/remoteimport", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return remote_import_backup_(self._request_adapter)
