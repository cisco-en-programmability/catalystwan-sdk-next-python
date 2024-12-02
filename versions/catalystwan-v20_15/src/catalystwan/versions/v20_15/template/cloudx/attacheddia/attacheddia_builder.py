# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import List, Any
from catalystwan.abc import RequestAdapterInterface


class AttacheddiaBuilder:
    """
    Builds and executes requests for operations under /template/cloudx/attacheddia
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_attached_dia_list(self, **kw) -> List[Any]:
        """
        Get attached Dia site list

        :returns: List[Any]
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/template/cloudx/attacheddia",
            return_type=List[Any],
            **kw,
        )
