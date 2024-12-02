# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from catalystwan.abc import RequestAdapterInterface


class DownloadBuilder:
    """
    Builds and executes requests for operations under /device/file-based/data-collection/download
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def download_generated_file(self, request_uuid: str, **kw) -> str:
        """
        Download generated file

        :param request_uuid: request UUID
        :returns: str
        """
        params = {
            "requestUUID": request_uuid,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/file-based/data-collection/download/{requestUUID}",
            return_type=str,
            params=params,
            **kw,
        )
