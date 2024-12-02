# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface
from .models import DownloadListPostRequest


class FilelistBuilder:
    """
    Builds and executes requests for operations under /statistics/download/{processType}/filelist
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def download_list(self):
        class download_list_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                process_type: str,
                payload: Optional[DownloadListPostRequest] = None,
                **kw,
            ):
                """
                Downloading list of stats file

                :param process_type: Possible types are: remoteprocessing, dr
                :param payload: Payload
                :returns: None
                """
                params = {
                    "processType": process_type,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/statistics/download/{processType}/filelist",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> DownloadListPostRequest:
                return DownloadListPostRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[DownloadListPostRequest]:
                return DownloadListPostRequest

        return download_list_(self._request_adapter)
