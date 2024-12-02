# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import List

from catalystwan.abc import RequestAdapterInterface

from .models import Loggers


class LoggersBuilder:
    """
    Builds and executes requests for operations under /util/logging/loggers
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def list_loggers(self, **kw) -> List[Loggers]:
        """
        List loggers

        :returns: List[Loggers]
        """
        return self._request_adapter.request(
            "GET", "/dataservice/util/logging/loggers", return_type=List[Loggers], **kw
        )
