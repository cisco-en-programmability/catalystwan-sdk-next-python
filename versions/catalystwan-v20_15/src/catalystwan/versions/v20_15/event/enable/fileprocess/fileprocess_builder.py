# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from .models import GeneralSchema


class FileprocessBuilder:
    """
    Builds and executes requests for operations under /event/enable/fileprocess
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def enable_events_from_file(self, **kw) -> GeneralSchema:
        """
        Enable events from file.

        :returns: GeneralSchema
        """
        return self._request_adapter.request(
            "GET", "/dataservice/event/enable/fileprocess", return_type=GeneralSchema, **kw
        )
