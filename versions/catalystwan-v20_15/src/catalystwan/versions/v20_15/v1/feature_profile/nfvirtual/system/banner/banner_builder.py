# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class BannerBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/nfvirtual/system/{systemId}/banner
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_nfvirtual_banner_parcel(
        self, system_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create Banner Profile Parcel for System feature profile

        :param system_id: Feature Profile ID
        :param payload: Banner config Profile Parcel
        :returns: str
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/nfvirtual/system/{systemId}/banner",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_nfvirtual_banner_parcel(self, system_id: str, banner_id: str, **kw) -> str:
        """
        Get Banner Profile Parcels for System feature profile

        :param system_id: Feature Profile ID
        :param banner_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "systemId": system_id,
            "bannerId": banner_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/nfvirtual/system/{systemId}/banner/{bannerId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_nfvirtual_banner_parcel(
        self, system_id: str, banner_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit a  Banner Profile Parcel for System feature profile

        :param system_id: Feature Profile ID
        :param banner_id: Profile Parcel ID
        :param payload: Banner Profile Parcel
        :returns: str
        """
        params = {
            "systemId": system_id,
            "bannerId": banner_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/nfvirtual/system/{systemId}/banner/{bannerId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_nfvirtual_banner_parcel(self, system_id: str, banner_id: str, **kw):
        """
        Delete a Banner Profile Parcel for System feature profile

        :param system_id: Feature Profile ID
        :param banner_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "systemId": system_id,
            "bannerId": banner_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/nfvirtual/system/{systemId}/banner/{bannerId}",
            params=params,
            **kw,
        )
