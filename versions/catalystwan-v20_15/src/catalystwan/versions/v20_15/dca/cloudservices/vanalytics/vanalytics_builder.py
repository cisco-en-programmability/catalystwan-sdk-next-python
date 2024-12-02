# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class VanalyticsBuilder:
    """
    Builds and executes requests for operations under /dca/cloudservices/vanalytics
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def getv_analytics(self):
        class getv_analytics_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[str] = None, **kw) -> Any:
                """
                Get session from DCS for vAnalytics

                :param payload: Payload
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/dca/cloudservices/vanalytics",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return getv_analytics_(self._request_adapter)
