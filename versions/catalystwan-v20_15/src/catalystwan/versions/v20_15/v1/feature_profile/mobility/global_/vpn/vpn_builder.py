# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface


class VpnBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/mobility/global/{profileId}/vpn
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_vpn_profile_parcel_for_mobility(self, profile_id: str, **kw) -> str:
        """
        Get VPN Profile Parcels for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :returns: str
        """
        params = {
            "profileId": profile_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/vpn",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_vpn_profile_parcel_for_mobility(self):
        class create_vpn_profile_parcel_for_mobility_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, profile_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Create a VPN Profile Parcel for Mobility Global Feature Profile

                :param profile_id: Feature Profile ID
                :param payload: VPN Profile Parcel
                :returns: str
                """
                params = {
                    "profileId": profile_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/mobility/global/{profileId}/vpn",
                    return_type=str,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return create_vpn_profile_parcel_for_mobility_(self._request_adapter)

    def get_vpn_profile_parcel_by_parcel_id_for_mobility(
        self, profile_id: str, vpn_id: str, **kw
    ) -> str:
        """
        Get VPN Profile Parcel by parcelId for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "profileId": profile_id,
            "vpnId": vpn_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/vpn/{vpnId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_vpn_profile_parcel_for_mobility(self):
        class edit_vpn_profile_parcel_for_mobility_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, profile_id: str, vpn_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Update a VPN Profile Parcel for Mobility Global Feature Profile

                :param profile_id: Feature Profile ID
                :param vpn_id: Profile Parcel ID
                :param payload: VPN Profile Parcel
                :returns: str
                """
                params = {
                    "profileId": profile_id,
                    "vpnId": vpn_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/mobility/global/{profileId}/vpn/{vpnId}",
                    return_type=str,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return edit_vpn_profile_parcel_for_mobility_(self._request_adapter)

    def delete_vpn_profile_parcel_for_mobility(
        self, profile_id: str, vpn_id: str, **kw
    ):
        """
        Delete a VPN Profile Parcel for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "profileId": profile_id,
            "vpnId": vpn_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/vpn/{vpnId}",
            params=params,
            **kw,
        )
