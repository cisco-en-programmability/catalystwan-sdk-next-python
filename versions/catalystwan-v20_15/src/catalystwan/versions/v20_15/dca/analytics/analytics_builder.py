# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .all.all_builder import AllBuilder


class AnalyticsBuilder:
    """
    Builds and executes requests for operations under /dca/analytics
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def create_stats(self):
        class create_stats_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw):
                """
                Update collection time of DCARest stat for vAnalytics

                :param payload: Stats query
                :returns: None
                """
                return self._request_adapter.request(
                    "PUT", "/dataservice/dca/analytics", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return create_stats_(self._request_adapter)

    @property
    def all(self) -> AllBuilder:
        """
        The all property
        """
        from .all.all_builder import AllBuilder

        return AllBuilder(self._request_adapter)
