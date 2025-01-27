# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import SetLogLevelPostRequest


class LevelBuilder:
    """
    Builds and executes requests for operations under /util/logging/level
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def set_log_level(self, payload: Optional[SetLogLevelPostRequest] = None, **kw):
        """
        Set log level for logger

        :param payload: Payload
        :returns: None
        """
        return self._request_adapter.request(
            "POST", "/dataservice/util/logging/level", payload=payload, **kw
        )
