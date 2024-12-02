# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface


class DownloadBuilder:
    """
    Builds and executes requests for operations under /backup/download
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def download_backup_file(self, path: str, **kw) -> str:
        """
        Download a Backup File that is already stored in vManage

        :param path: Path
        :returns: str
        """
        params = {
            "path": path,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/backup/download/{path}",
            return_type=str,
            params=params,
            **kw,
        )
