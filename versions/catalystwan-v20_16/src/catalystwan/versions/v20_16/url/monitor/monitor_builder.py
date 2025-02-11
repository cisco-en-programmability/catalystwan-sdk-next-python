# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import UrlMonitoringInfoInner


class MonitorBuilder:
    """
    Builds and executes requests for operations under /url/monitor
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_url_monitor(self, **kw) -> List[UrlMonitoringInfoInner]:
        """
        List url's with monitoring configuration and details about the current state of alarm.

        :returns: List[UrlMonitoringInfoInner]
        """
        return self._request_adapter.request(
            "GET", "/dataservice/url/monitor", return_type=List[UrlMonitoringInfoInner], **kw
        )

    def update_url_monitor(self, payload: Optional[Any] = None, **kw):
        """
        Update monitor configuration related to the url

        :param payload: Payload
        :returns: None
        """
        return self._request_adapter.request(
            "PUT", "/dataservice/url/monitor", payload=payload, **kw
        )

    def create_url_monitor(self, payload: Optional[Any] = None, **kw):
        """
        Monitor the url with specified configuration.

        :param payload: Payload
        :returns: None
        """
        return self._request_adapter.request(
            "POST", "/dataservice/url/monitor", payload=payload, **kw
        )

    def delete_url_monitor(self, url: str, **kw):
        """
        Delete an url which is already being monitored.

        :param url: url to delete
        :returns: None
        """
        params = {
            "url": url,
        }
        return self._request_adapter.request(
            "DELETE", "/dataservice/url/monitor", params=params, **kw
        )
