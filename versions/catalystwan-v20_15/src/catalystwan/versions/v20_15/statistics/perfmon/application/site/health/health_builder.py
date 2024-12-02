# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import ApplicationSiteItem, HealthParam


class HealthBuilder:
    """
    Builds and executes requests for operations under /statistics/perfmon/application/site/health
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_application_site_health(self):
        class get_application_site_health_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                payload: Optional[Any] = None,
                health: Optional[HealthParam] = None,
                **kw,
            ) -> List[ApplicationSiteItem]:
                """
                Get one application health for one site

                :param health: Health
                :param payload: Stats query string
                :returns: List[ApplicationSiteItem]
                """
                params = {
                    "health": health,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/statistics/perfmon/application/site/health",
                    return_type=List[ApplicationSiteItem],
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return get_application_site_health_(self._request_adapter)
