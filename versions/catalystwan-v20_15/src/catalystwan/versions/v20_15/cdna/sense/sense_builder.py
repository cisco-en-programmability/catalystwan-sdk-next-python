# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from .models import DnaSenseResponse


class SenseBuilder:
    """
    Builds and executes requests for operations under /cdna/sense
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_cdna_sense_service(self, tag: str, **kw) -> DnaSenseResponse:
        """
        Get Sense Service

        :param tag: Tag
        :returns: DnaSenseResponse
        """
        params = {
            "tag": tag,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/cdna/sense/{tag}",
            return_type=DnaSenseResponse,
            params=params,
            **kw,
        )
