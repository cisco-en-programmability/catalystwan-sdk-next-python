# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface
from .models import CreateEthernetProfileParcelForMobilityPostRequest


class EthernetBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/mobility/global/{profileId}/ethernet
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_ethernet_profile_parcels(self, profile_id: str, **kw) -> str:
        """
        Get Ethernet Profile Parcels for feature profile

        :param profile_id: Feature Profile ID
        :returns: str
        """
        params = {
            "profileId": profile_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/ethernet",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_ethernet_profile_parcel_for_mobility(self):
        class create_ethernet_profile_parcel_for_mobility_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                profile_id: str,
                payload: Optional[
                    CreateEthernetProfileParcelForMobilityPostRequest
                ] = None,
                **kw,
            ) -> str:
                """
                Create an ethernet Profile Parcel for Mobility Global Feature Profile

                :param profile_id: Feature Profile ID
                :param payload: Ethernet Profile Parcel
                :returns: str
                """
                params = {
                    "profileId": profile_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/mobility/global/{profileId}/ethernet",
                    return_type=str,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(
                self, *args, **kwargs
            ) -> CreateEthernetProfileParcelForMobilityPostRequest:
                return CreateEthernetProfileParcelForMobilityPostRequest(
                    *args, **kwargs
                )

            @property
            def payload_model(
                self,
            ) -> Type[CreateEthernetProfileParcelForMobilityPostRequest]:
                return CreateEthernetProfileParcelForMobilityPostRequest

        return create_ethernet_profile_parcel_for_mobility_(self._request_adapter)

    def get_ethernet_profile_parcel(
        self, profile_id: str, ethernet_id: str, **kw
    ) -> str:
        """
        Get Ethernet Profile Parcels for feature profile

        :param profile_id: Feature Profile ID
        :param ethernet_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "profileId": profile_id,
            "ethernetId": ethernet_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/ethernet/{ethernetId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_ethernet_profile_parcel_for_system(self):
        class edit_ethernet_profile_parcel_for_system_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                profile_id: str,
                ethernet_id: str,
                payload: Optional[str] = None,
                **kw,
            ):
                """
                Update a Ethernet Profile Parcel for feature profile

                :param profile_id: Feature Profile ID
                :param ethernet_id: Profile Parcel ID
                :param payload: Ethernet Profile Parcel
                :returns: None
                """
                params = {
                    "profileId": profile_id,
                    "ethernetId": ethernet_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/mobility/global/{profileId}/ethernet/{ethernetId}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return edit_ethernet_profile_parcel_for_system_(self._request_adapter)

    def delete_ethernet_profile_parcel_for_system(
        self, profile_id: str, ethernet_id: str, **kw
    ):
        """
        Delete a Ethernet Profile Parcel for feature profile

        :param profile_id: Feature Profile ID
        :param ethernet_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "profileId": profile_id,
            "ethernetId": ethernet_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/ethernet/{ethernetId}",
            params=params,
            **kw,
        )
