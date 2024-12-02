# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import List
from catalystwan.abc import RequestAdapterInterface
from .models import AppRouteDocCountResponse


class FieldsBuilder:
    """
    Builds and executes requests for operations under /statistics/approute/fields
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_stat_data_fields_3(self, **kw) -> List[AppRouteDocCountResponse]:
        """
        Get fields and type

        :returns: List[AppRouteDocCountResponse]
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/statistics/approute/fields",
            return_type=List[AppRouteDocCountResponse],
            **kw,
        )
