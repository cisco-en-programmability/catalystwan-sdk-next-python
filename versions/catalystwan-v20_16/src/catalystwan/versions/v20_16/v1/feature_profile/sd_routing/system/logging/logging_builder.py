# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class LoggingBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/system/{systemId}/logging
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdrouting_logging_features(self, system_id: str, **kw) -> str:
        """
        Get all SD-Routing Logging features from a specific system feature profile

        :param system_id: System Profile ID
        :returns: str
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/system/{systemId}/logging",
            return_type=str,
            params=params,
            **kw,
        )

    def create_sdrouting_logging_feature(
        self, system_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a SD-Routing Logging feature from a specific system feature profile

        :param system_id: System Profile ID
        :param payload: SD-Routing Logging feature from a specific system feature profile
        :returns: str
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/system/{systemId}/logging",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_sdrouting_logging_feature(self, system_id: str, logging_id: str, **kw) -> str:
        """
        Get the SD-Routing Logging feature from a specific system feature profile

        :param system_id: System Profile ID
        :param logging_id: Logging Feature ID
        :returns: str
        """
        params = {
            "systemId": system_id,
            "loggingId": logging_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/system/{systemId}/logging/{loggingId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_sdrouting_logging_feature(
        self, system_id: str, logging_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit the SD-Routing Logging feature from a specific system feature profile

        :param system_id: System Profile ID
        :param logging_id: Logging Feature ID
        :param payload: SD-Routing Logging feature from a specific system feature profile
        :returns: str
        """
        params = {
            "systemId": system_id,
            "loggingId": logging_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/system/{systemId}/logging/{loggingId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sdrouting_logging_feature(self, system_id: str, logging_id: str, **kw):
        """
        Delete the SD-Routing Logging feature from a specific system feature profile

        :param system_id: System Profile ID
        :param logging_id: Logging Feature ID
        :returns: None
        """
        params = {
            "systemId": system_id,
            "loggingId": logging_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/system/{systemId}/logging/{loggingId}",
            params=params,
            **kw,
        )
