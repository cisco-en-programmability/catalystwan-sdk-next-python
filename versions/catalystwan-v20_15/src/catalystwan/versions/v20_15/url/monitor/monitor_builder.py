# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import UrlMonitoringInfoInner


class MonitorBuilder:
    """
    Builds and executes requests for operations under /url/monitor
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_url_monitor(self, **kw) -> List[UrlMonitoringInfoInner]:
        """
        List url's with monitoring configuration and details about the current state of alarm.

        :returns: List[UrlMonitoringInfoInner]
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/url/monitor",
            return_type=List[UrlMonitoringInfoInner],
            **kw,
        )

    @property
    def update_url_monitor(self):
        class update_url_monitor_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw):
                """
                Update monitor configuration related to the url

                :param payload: Payload
                :returns: None
                """
                return self._request_adapter.request(
                    "PUT", "/dataservice/url/monitor", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return update_url_monitor_(self._request_adapter)

    @property
    def create_url_monitor(self):
        class create_url_monitor_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw):
                """
                Monitor the url with specified configuration.

                :param payload: Payload
                :returns: None
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/url/monitor", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return create_url_monitor_(self._request_adapter)

    def delete_url_monitor(self, url: str, **kw):
        """
        Delete an url which is already being monitored.

        :param url: Url
        :returns: None
        """
        params = {
            "url": url,
        }
        return self._request_adapter.request(
            "DELETE", "/dataservice/url/monitor", params=params, **kw
        )
