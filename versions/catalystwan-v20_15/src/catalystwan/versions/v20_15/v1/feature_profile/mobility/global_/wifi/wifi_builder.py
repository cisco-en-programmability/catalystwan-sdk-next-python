# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import CreateWifiProfileParcelForMobilityPostRequest


class WifiBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/mobility/global/{profileId}/wifi
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_wifi_profile_parcel_list_for_mobility(self, profile_id: str, **kw) -> str:
        """
        Get Wifi Profile Parcel List for Mobility feature profile

        :param profile_id: Feature Profile ID
        :returns: str
        """
        params = {
            "profileId": profile_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/wifi",
            return_type=str,
            params=params,
            **kw,
        )

    def create_wifi_profile_parcel_for_mobility(
        self,
        profile_id: str,
        payload: Optional[CreateWifiProfileParcelForMobilityPostRequest] = None,
        **kw,
    ) -> str:
        """
        Create an Wifi Profile Parcel for Mobility feature profile

        :param profile_id: Feature Profile ID
        :param payload: Wifi Profile Parcel
        :returns: str
        """
        params = {
            "profileId": profile_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/wifi",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_wifi_profile_parcel_for_mobility(self, profile_id: str, wifi_id: str, **kw) -> str:
        """
        Get an Wifi Profile Parcel for Mobility feature profile

        :param profile_id: Feature Profile ID
        :param wifi_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "profileId": profile_id,
            "wifiId": wifi_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/wifi/{wifiId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_wifi_profile_parcel_for_mobility(
        self,
        profile_id: str,
        wifi_id: str,
        payload: Optional[CreateWifiProfileParcelForMobilityPostRequest] = None,
        **kw,
    ):
        """
        Edit an Wifi Profile Parcel for Mobility feature profile

        :param profile_id: Feature Profile ID
        :param wifi_id: Profile Parcel ID
        :param payload: Wifi Profile Parcel
        :returns: None
        """
        params = {
            "profileId": profile_id,
            "wifiId": wifi_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/wifi/{wifiId}",
            params=params,
            payload=payload,
            **kw,
        )

    def delete_wifi_profile_parcel_for_mobility(self, profile_id: str, wifi_id: str, **kw):
        """
        Delete an Wifi Profile Parcel for Mobility feature profile

        :param profile_id: Feature Profile ID
        :param wifi_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "profileId": profile_id,
            "wifiId": wifi_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/wifi/{wifiId}",
            params=params,
            **kw,
        )
