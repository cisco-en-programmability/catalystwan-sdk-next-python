# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Any
from catalystwan.abc import RequestAdapterInterface


class DownloadBuilder:
    """
    Builds and executes requests for operations under /device/tools/admintech/download
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def download_admin_tech_file(self, filename: str, **kw) -> Any:
        """
        Download admin tech logs

        :param filename: Admin tech file
        :returns: Any
        """
        params = {
            "filename": filename,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/tools/admintech/download/{filename}",
            params=params,
            **kw,
        )
