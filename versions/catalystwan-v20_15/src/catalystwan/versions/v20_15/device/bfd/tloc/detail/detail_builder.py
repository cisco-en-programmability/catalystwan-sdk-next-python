# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any
from catalystwan.abc import RequestAdapterInterface
from .models import StateParam


class DetailBuilder:
    """
    Builds and executes requests for operations under /device/bfd/tloc/detail
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_bfd_tloc_state_detail(
        self, state: Optional[StateParam] = None, **kw
    ) -> Any:
        """
        Get detailed BFD tloc details

        :param state: State
        :returns: Any
        """
        params = {
            "state": state,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/device/bfd/tloc/detail", params=params, **kw
        )
