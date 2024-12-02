# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import GetO365PreferredPathFromVAnalyticsPostRequest


class PreferredpathBuilder:
    """
    Builds and executes requests for operations under /cloudservices/m365/preferredpath
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_o365_preferred_path_from_v_analytics(self):
        class get_o365_preferred_path_from_v_analytics_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                payload: Optional[GetO365PreferredPathFromVAnalyticsPostRequest] = None,
                **kw,
            ):
                """
                Get vAnalytics Preferred Path for Office365 over time. The data can be filtered on time and other unique parameters based upon necessity and intended usage

                :param payload: Payload
                :returns: None
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/cloudservices/m365/preferredpath",
                    payload=payload,
                    **kw,
                )

            def create_payload(
                self, *args, **kwargs
            ) -> GetO365PreferredPathFromVAnalyticsPostRequest:
                return GetO365PreferredPathFromVAnalyticsPostRequest(*args, **kwargs)

            @property
            def payload_model(
                self,
            ) -> Type[GetO365PreferredPathFromVAnalyticsPostRequest]:
                return GetO365PreferredPathFromVAnalyticsPostRequest

        return get_o365_preferred_path_from_v_analytics_(self._request_adapter)
