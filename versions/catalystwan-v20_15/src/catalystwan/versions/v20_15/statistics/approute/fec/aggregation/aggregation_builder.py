# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List, Any, Type
from catalystwan.abc import RequestAdapterInterface
from .models import AppRouteFecAggRespInner


class AggregationBuilder:
    """
    Builds and executes requests for operations under /statistics/approute/fec/aggregation
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_app_route_fec_agg(self):
        class get_app_route_fec_agg_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[Any] = None, site_id: Optional[str] = None, **kw
            ) -> List[AppRouteFecAggRespInner]:
                """
                Get aggregation data and fec recovery rate

                :param site_id: Site id
                :param payload: Query filter
                :returns: List[AppRouteFecAggRespInner]
                """
                params = {
                    "site-id": site_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/statistics/approute/fec/aggregation",
                    return_type=List[AppRouteFecAggRespInner],
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return get_app_route_fec_agg_(self._request_adapter)
