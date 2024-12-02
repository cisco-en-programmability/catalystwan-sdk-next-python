# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface
from .models import DpiResponse
from .models import SortOrderParam

if TYPE_CHECKING:
    from .agg_app.agg_app_builder import AggAppBuilder
    from .aggregation.aggregation_builder import AggregationBuilder
    from .applications.applications_builder import ApplicationsBuilder
    from .csv.csv_builder import CsvBuilder
    from .device.device_builder import DeviceBuilder
    from .doccount.doccount_builder import DoccountBuilder
    from .fields.fields_builder import FieldsBuilder
    from .page.page_builder import PageBuilder
    from .pktdup.pktdup_builder import PktdupBuilder
    from .query.query_builder import QueryBuilder
    from .recovery.recovery_builder import RecoveryBuilder


class DpiBuilder:
    """
    Builds and executes requests for operations under /statistics/dpi
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_dpi_stats_raw_data(
        self,
        query: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[SortOrderParam] = None,
        **kw,
    ) -> DpiResponse:
        """
        Get DPI stats raw data

        :param query: Query
        :param page: Page
        :param page_size: Page size
        :param sort_by: Sort by
        :param sort_order: Sort order
        :returns: DpiResponse
        """
        params = {
            "query": query,
            "page": page,
            "pageSize": page_size,
            "sortBy": sort_by,
            "sortOrder": sort_order,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/statistics/dpi",
            return_type=DpiResponse,
            params=params,
            **kw,
        )

    @property
    def get_dpi_stats_raw_data_post(self):
        class get_dpi_stats_raw_data_post_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                payload: Optional[Any] = None,
                page: Optional[int] = None,
                page_size: Optional[int] = None,
                sort_by: Optional[str] = None,
                sort_order: Optional[SortOrderParam] = None,
                **kw,
            ) -> DpiResponse:
                """
                Get DPI stats raw data

                :param page: Page
                :param page_size: Page size
                :param sort_by: Sort by
                :param sort_order: Sort order
                :param payload: User
                :returns: DpiResponse
                """
                params = {
                    "page": page,
                    "pageSize": page_size,
                    "sortBy": sort_by,
                    "sortOrder": sort_order,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/statistics/dpi",
                    return_type=DpiResponse,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return get_dpi_stats_raw_data_post_(self._request_adapter)

    @property
    def agg_app(self) -> AggAppBuilder:
        """
        The agg-app property
        """
        from .agg_app.agg_app_builder import AggAppBuilder

        return AggAppBuilder(self._request_adapter)

    @property
    def aggregation(self) -> AggregationBuilder:
        """
        The aggregation property
        """
        from .aggregation.aggregation_builder import AggregationBuilder

        return AggregationBuilder(self._request_adapter)

    @property
    def applications(self) -> ApplicationsBuilder:
        """
        The applications property
        """
        from .applications.applications_builder import ApplicationsBuilder

        return ApplicationsBuilder(self._request_adapter)

    @property
    def csv(self) -> CsvBuilder:
        """
        The csv property
        """
        from .csv.csv_builder import CsvBuilder

        return CsvBuilder(self._request_adapter)

    @property
    def device(self) -> DeviceBuilder:
        """
        The device property
        """
        from .device.device_builder import DeviceBuilder

        return DeviceBuilder(self._request_adapter)

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
    def pktdup(self) -> PktdupBuilder:
        """
        The pktdup property
        """
        from .pktdup.pktdup_builder import PktdupBuilder

        return PktdupBuilder(self._request_adapter)

    @property
    def query(self) -> QueryBuilder:
        """
        The query property
        """
        from .query.query_builder import QueryBuilder

        return QueryBuilder(self._request_adapter)

    @property
    def recovery(self) -> RecoveryBuilder:
        """
        The recovery property
        """
        from .recovery.recovery_builder import RecoveryBuilder

        return RecoveryBuilder(self._request_adapter)
