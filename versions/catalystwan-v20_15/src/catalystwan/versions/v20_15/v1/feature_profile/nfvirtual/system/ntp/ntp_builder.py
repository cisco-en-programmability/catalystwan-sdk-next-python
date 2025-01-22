# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class NtpBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/nfvirtual/system/{systemId}/ntp
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_nfvirtual_ntp_parcel(
        self, system_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create NTP Profile Parcel for System feature profile

        :param system_id: Feature Profile ID
        :param payload: NTP config Profile Parcel
        :returns: str
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/nfvirtual/system/{systemId}/ntp",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_nfvirtual_ntp_parcel(self, system_id: str, ntp_id: str, **kw) -> str:
        """
        Get NTP Profile Parcels for System feature profile

        :param system_id: Feature Profile ID
        :param ntp_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "systemId": system_id,
            "ntpId": ntp_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/nfvirtual/system/{systemId}/ntp/{ntpId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_nfvirtual_ntp_parcel(
        self, system_id: str, ntp_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit a  NTP Profile Parcel for System feature profile

        :param system_id: Feature Profile ID
        :param ntp_id: Profile Parcel ID
        :param payload: NTP Profile Parcel
        :returns: str
        """
        params = {
            "systemId": system_id,
            "ntpId": ntp_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/nfvirtual/system/{systemId}/ntp/{ntpId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_nfvirtual_ntp_parcel(self, system_id: str, ntp_id: str, **kw):
        """
        Delete a NTP Profile Parcel for System feature profile

        :param system_id: Feature Profile ID
        :param ntp_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "systemId": system_id,
            "ntpId": ntp_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/nfvirtual/system/{systemId}/ntp/{ntpId}",
            params=params,
            **kw,
        )
