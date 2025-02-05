# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class BannerBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/system/{systemId}/banner
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdrouting_banner_features(self, system_id: str, **kw) -> str:
        """
        Get all SD-Routing banner features from a specific system feature profile

        :param system_id: System Profile ID
        :returns: str
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/system/{systemId}/banner",
            return_type=str,
            params=params,
            **kw,
        )

    def create_sdrouting_banner_feature(
        self, system_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a SD-Routing banner feature from a specific system feature profile

        :param system_id: System Profile ID
        :param payload: SD-Routing banner feature from a specific system feature profile
        :returns: str
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/system/{systemId}/banner",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_sdrouting_banner_feature(self, system_id: str, banner_id: str, **kw) -> str:
        """
        Get the SD-Routing banner feature from a specific system feature profile

        :param system_id: System Profile ID
        :param banner_id: Banner Feature ID
        :returns: str
        """
        params = {
            "systemId": system_id,
            "bannerId": banner_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/system/{systemId}/banner/{bannerId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_sdrouting_banner_feature(
        self, system_id: str, banner_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit the SD-Routing banner feature from a specific system feature profile

        :param system_id: System Profile ID
        :param banner_id: Banner Feature ID
        :param payload: SD-Routing banner feature from a specific system feature profile
        :returns: str
        """
        params = {
            "systemId": system_id,
            "bannerId": banner_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/system/{systemId}/banner/{bannerId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sdrouting_banner_feature(self, system_id: str, banner_id: str, **kw):
        """
        Delete the SD-Routing banner feature from a specific system feature profile

        :param system_id: System Profile ID
        :param banner_id: Banner Feature ID
        :returns: None
        """
        params = {
            "systemId": system_id,
            "bannerId": banner_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/system/{systemId}/banner/{bannerId}",
            params=params,
            **kw,
        )
