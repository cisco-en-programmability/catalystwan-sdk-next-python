# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class AaaBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/nfvirtual/system/{systemId}/aaa
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_nfvirtual_aaa_parcel(
        self, system_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create AAA Profile Parcel for System feature profile

        :param system_id: Feature Profile ID
        :param payload: AAA config Profile Parcel
        :returns: str
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/nfvirtual/system/{systemId}/aaa",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_nfvirtual_aaa_parcel(self, system_id: str, aaa_id: str, **kw) -> str:
        """
        Get AAA Profile Parcels for System feature profile

        :param system_id: Feature Profile ID
        :param aaa_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "systemId": system_id,
            "aaaId": aaa_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/nfvirtual/system/{systemId}/aaa/{aaaId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_nfvirtual_aaa_parcel(
        self, system_id: str, aaa_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit a  AAA Profile Parcel for System feature profile

        :param system_id: Feature Profile ID
        :param aaa_id: Profile Parcel ID
        :param payload: AAA Profile Parcel
        :returns: str
        """
        params = {
            "systemId": system_id,
            "aaaId": aaa_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/nfvirtual/system/{systemId}/aaa/{aaaId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_nfvirtual_aaa_parcel(self, system_id: str, aaa_id: str, **kw):
        """
        Delete a AAA Profile Parcel for System feature profile

        :param system_id: Feature Profile ID
        :param aaa_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "systemId": system_id,
            "aaaId": aaa_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/nfvirtual/system/{systemId}/aaa/{aaaId}",
            params=params,
            **kw,
        )
