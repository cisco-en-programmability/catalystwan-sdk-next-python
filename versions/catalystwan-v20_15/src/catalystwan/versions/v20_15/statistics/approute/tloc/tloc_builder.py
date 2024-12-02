# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import AppRouteTlocRespInner


class TlocBuilder:
    """
    Builds and executes requests for operations under /statistics/approute/tloc
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_approute_tloc(self, payload: Optional[Any] = None, **kw) -> List[AppRouteTlocRespInner]:
        """
        Get tloc

        :param payload: Query filter
        :returns: List[AppRouteTlocRespInner]
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/statistics/approute/tloc",
            return_type=List[AppRouteTlocRespInner],
            payload=payload,
            **kw,
        )
