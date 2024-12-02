# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import GetAuditLogData

if TYPE_CHECKING:
    from .aggregation.aggregation_builder import AggregationBuilder
    from .doccount.doccount_builder import DoccountBuilder
    from .fields.fields_builder import FieldsBuilder
    from .page.page_builder import PageBuilder
    from .query.query_builder import QueryBuilder
    from .severity.severity_builder import SeverityBuilder


class AuditlogBuilder:
    """
    Builds and executes requests for operations under /auditlog
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_stat_data_raw_audit_log_data(self, query: str, **kw) -> GetAuditLogData:
        """
        Get stat raw data

        :param query: Query
        :returns: GetAuditLogData
        """
        params = {
            "query": query,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/auditlog",
            return_type=GetAuditLogData,
            params=params,
            **kw,
        )

    @property
    def get_raw_property_data(self):
        class get_raw_property_data_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> GetAuditLogData:
                """
                Get raw property data with post action

                :param payload: Stats query string
                :returns: GetAuditLogData
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/auditlog",
                    return_type=GetAuditLogData,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return get_raw_property_data_(self._request_adapter)

    @property
    def aggregation(self) -> AggregationBuilder:
        """
        The aggregation property
        """
        from .aggregation.aggregation_builder import AggregationBuilder

        return AggregationBuilder(self._request_adapter)

    @property
    def doccount(self) -> DoccountBuilder:
        """
        The doccount property
        """
        from .doccount.doccount_builder import DoccountBuilder

        return DoccountBuilder(self._request_adapter)

    @property
    def fields(self) -> FieldsBuilder:
        """
        The fields property
        """
        from .fields.fields_builder import FieldsBuilder

        return FieldsBuilder(self._request_adapter)

    @property
    def page(self) -> PageBuilder:
        """
        The page property
        """
        from .page.page_builder import PageBuilder

        return PageBuilder(self._request_adapter)

    @property
    def query(self) -> QueryBuilder:
        """
        The query property
        """
        from .query.query_builder import QueryBuilder

        return QueryBuilder(self._request_adapter)

    @property
    def severity(self) -> SeverityBuilder:
        """
        The severity property
        """
        from .severity.severity_builder import SeverityBuilder

        return SeverityBuilder(self._request_adapter)
