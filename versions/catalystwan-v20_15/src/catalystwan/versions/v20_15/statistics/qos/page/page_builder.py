# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import QoSRespWithPageInfo


class PageBuilder:
    """
    Builds and executes requests for operations under /statistics/qos/page
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_stat_bulk_raw_data_3(
        self,
        query: Optional[str] = None,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
        **kw,
    ) -> QoSRespWithPageInfo:
        """
        Get stats raw data

        :param query: Query
        :param scroll_id: Scroll id
        :param count: Count
        :returns: QoSRespWithPageInfo
        """
        params = {
            "query": query,
            "scrollId": scroll_id,
            "count": count,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/statistics/qos/page",
            return_type=QoSRespWithPageInfo,
            params=params,
            **kw,
        )

    @property
    def get_post_stat_bulk_raw_data12(self):
        class get_post_stat_bulk_raw_data12_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                payload: Optional[Any] = None,
                scroll_id: Optional[str] = None,
                count: Optional[int] = None,
                **kw,
            ) -> QoSRespWithPageInfo:
                """
                Get stats raw data

                :param scroll_id: Scroll id
                :param count: Count
                :param payload: Stats query string
                :returns: QoSRespWithPageInfo
                """
                params = {
                    "scrollId": scroll_id,
                    "count": count,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/statistics/qos/page",
                    return_type=QoSRespWithPageInfo,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return get_post_stat_bulk_raw_data12_(self._request_adapter)
