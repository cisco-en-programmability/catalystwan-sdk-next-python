# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class MulticloudConnectionBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/transport/{transportId}/multicloud-connection
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_lan_vpn_profile_parcel_for_service_1(self, transport_id: str, **kw) -> str:
        """
        Get Lan Vpn Profile Parcels for Service feature profile

        :param transport_id: Feature Profile ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/multicloud-connection",
            return_type=str,
            params=params,
            **kw,
        )

    def create_multi_cloud_connection_1(
        self, transport_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Associate a MultiCloudConnection Parcel for transport feature profile

        :param transport_id: Feature Profile ID
        :param payload: MultiConnection Extension Payload for defining the multicloud connection to the cloud gateway
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/multicloud-connection",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_lan_vpn_profile_parcel_by_parcel_id_for_service_1(
        self, transport_id: str, multi_cloud_connection_id: str, **kw
    ) -> str:
        """
        Get Lan Vpn Profile Parcel by parcelId for Service feature profile

        :param transport_id: Feature Profile ID
        :param multi_cloud_connection_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "multiCloudConnectionId": multi_cloud_connection_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/multicloud-connection/{multiCloudConnectionId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_multi_cloud_connection_1(
        self, transport_id: str, multi_cloud_connection_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Update a multicloud connection parcel

        :param transport_id: Feature Profile ID
        :param multi_cloud_connection_id: Profile Parcel ID
        :param payload: Multicloud Connection Profile Parcel
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "multiCloudConnectionId": multi_cloud_connection_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/multicloud-connection/{multiCloudConnectionId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_multi_cloud_connection_parcel_for_transport(
        self, transport_id: str, multi_cloud_connection_id: str, **kw
    ):
        """
        Delete a MultiCloud Connection Profile Parcel for Transport feature profile

        :param transport_id: Feature Profile ID
        :param multi_cloud_connection_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "multiCloudConnectionId": multi_cloud_connection_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/multicloud-connection/{multiCloudConnectionId}",
            params=params,
            **kw,
        )
