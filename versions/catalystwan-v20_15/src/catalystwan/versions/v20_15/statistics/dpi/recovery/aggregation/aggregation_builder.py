# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface
from .models import FecAndPktDupResponse


class AggregationBuilder:
    """
    Builds and executes requests for operations under /statistics/dpi/recovery/aggregation
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_dpi_stats_aggregation_data_for_fec(self):
        class get_dpi_stats_aggregation_data_for_fec_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[Any] = None, **kw
            ) -> FecAndPktDupResponse:
                """
                Get aggregation data and fec recovery rate if available

                :param payload: User
                :returns: FecAndPktDupResponse
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/statistics/dpi/recovery/aggregation",
                    return_type=FecAndPktDupResponse,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return get_dpi_stats_aggregation_data_for_fec_(self._request_adapter)
