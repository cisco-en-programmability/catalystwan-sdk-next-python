# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import GetAuditLogData


class PageBuilder:
    """
    Builds and executes requests for operations under /auditlog/page
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_stat_bulk_raw_property_data(
        self, query: str, count: int, scroll_id: Optional[str] = None, **kw
    ) -> GetAuditLogData:
        """
        Get raw property data in bulk

        :param query: Query
        :param scroll_id: Scroll id
        :param count: Count
        :returns: GetAuditLogData
        """
        params = {
            "query": query,
            "scrollId": scroll_id,
            "count": count,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/auditlog/page",
            return_type=GetAuditLogData,
            params=params,
            **kw,
        )

    @property
    def get_post_stat_bulk_raw_property_data(self):
        class get_post_stat_bulk_raw_property_data_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                count: int,
                payload: Optional[Any] = None,
                scroll_id: Optional[str] = None,
                **kw,
            ) -> GetAuditLogData:
                """
                Get raw property data in bulk with post action

                :param scroll_id: Scroll id
                :param count: Count
                :param payload: Stats query string
                :returns: GetAuditLogData
                """
                params = {
                    "scrollId": scroll_id,
                    "count": count,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/auditlog/page",
                    return_type=GetAuditLogData,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return get_post_stat_bulk_raw_property_data_(self._request_adapter)
