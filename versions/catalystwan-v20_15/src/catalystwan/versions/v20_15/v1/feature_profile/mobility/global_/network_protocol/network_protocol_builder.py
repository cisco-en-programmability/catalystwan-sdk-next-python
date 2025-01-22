# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import CreateNetworkProtocolProfileParcelForMobilityPostRequest


class NetworkProtocolBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/mobility/global/{profileId}/networkProtocol
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_network_protocol_profile_parcel_list_for_mobility(self, profile_id: str, **kw) -> str:
        """
        Get an Mobility NetworkProtocol Profile Parcel list for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :returns: str
        """
        params = {
            "profileId": profile_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/networkProtocol",
            return_type=str,
            params=params,
            **kw,
        )

    def create_network_protocol_profile_parcel_for_mobility(
        self,
        profile_id: str,
        payload: Optional[CreateNetworkProtocolProfileParcelForMobilityPostRequest] = None,
        **kw,
    ) -> str:
        """
        Create an NetworkProtocol Profile Parcel for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :param payload: NetworkProtocol Profile Parcel
        :returns: str
        """
        params = {
            "profileId": profile_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/networkProtocol",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_network_protocol_profile_parcel_for_mobility(
        self, profile_id: str, network_protocol_id: str, **kw
    ) -> str:
        """
        Get an Mobility NetworkProtocol Profile Parcel for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :param network_protocol_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "profileId": profile_id,
            "networkProtocolId": network_protocol_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/networkProtocol/{networkProtocolId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_network_protocol_profile_parcel_for_mobility(
        self,
        profile_id: str,
        network_protocol_id: str,
        payload: Optional[CreateNetworkProtocolProfileParcelForMobilityPostRequest] = None,
        **kw,
    ):
        """
        Edit an Network Protocol Profile Parcel for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :param network_protocol_id: Profile Parcel ID
        :param payload: Network Protocol Profile Parcel
        :returns: None
        """
        params = {
            "profileId": profile_id,
            "networkProtocolId": network_protocol_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/networkProtocol/{networkProtocolId}",
            params=params,
            payload=payload,
            **kw,
        )

    def delete_network_protocol_profile_parcel_for_mobility(
        self, profile_id: str, network_protocol_id: str, **kw
    ):
        """
        Delete a Network Protocol Profile Parcel for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :param network_protocol_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "profileId": profile_id,
            "networkProtocolId": network_protocol_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/networkProtocol/{networkProtocolId}",
            params=params,
            **kw,
        )
