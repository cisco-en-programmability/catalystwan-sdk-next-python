# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class ClouddiscoveredappBuilder:
    """
    Builds and executes requests for operations under /template/policy/clouddiscoveredapp
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_cloud_discovered_apps(self, **kw) -> List[Any]:
        """
        Get all cloud discovered applications

        :returns: List[Any]
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/template/policy/clouddiscoveredapp",
            return_type=List[Any],
            **kw,
        )

    @property
    def map_traffic_profiles(self):
        class map_traffic_profiles_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Set SLA class for policy cloud discovered applications

                :param payload: App payload
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/template/policy/clouddiscoveredapp",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return map_traffic_profiles_(self._request_adapter)
