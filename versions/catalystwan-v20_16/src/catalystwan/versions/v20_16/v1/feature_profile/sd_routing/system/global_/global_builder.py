# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class GlobalBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/system/{systemId}/global
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdrouting_global_setting_features(self, system_id: str, **kw) -> str:
        """
        Get all SD-Routing global setting features from a specific system feature profile

        :param system_id: System Profile ID
        :returns: str
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/system/{systemId}/global",
            return_type=str,
            params=params,
            **kw,
        )

    def create_sdrouting_global_setting_feature(
        self, system_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a SD-Routing global setting feature from a specific system feature profile

        :param system_id: System Profile ID
        :param payload: SD-Routing global setting feature from a specific system feature profile
        :returns: str
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/system/{systemId}/global",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_sdrouting_global_setting_feature(self, system_id: str, global_id: str, **kw) -> str:
        """
        Get the SD-Routing global setting feature from a specific system feature profile

        :param system_id: System Profile ID
        :param global_id: Global Setting Feature ID
        :returns: str
        """
        params = {
            "systemId": system_id,
            "globalId": global_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/system/{systemId}/global/{globalId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_sdrouting_global_setting_feature(
        self, system_id: str, global_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit the SD-Routing global setting feature from a specific system feature profile

        :param system_id: System Profile ID
        :param global_id: Global Setting Feature ID
        :param payload: SD-Routing global setting feature from a specific system feature profile
        :returns: str
        """
        params = {
            "systemId": system_id,
            "globalId": global_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/system/{systemId}/global/{globalId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sdrouting_global_setting_feature(self, system_id: str, global_id: str, **kw):
        """
        Delete the SD-Routing global setting feature from a specific system feature profile

        :param system_id: System Profile ID
        :param global_id: Global Setting Feature ID
        :returns: None
        """
        params = {
            "systemId": system_id,
            "globalId": global_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/system/{systemId}/global/{globalId}",
            params=params,
            **kw,
        )
