# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class CellularProfileBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/transport/{transportId}/cellular-controller/{cellularControllerId}/cellular-profile
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_cellular_controller_associated_cellular_profile_parcels_for_transport_1(
        self, transport_id: str, cellular_controller_id: str, **kw
    ) -> str:
        """
        Get CellularController associated Cellular Profile Features for transport feature profile

        :param transport_id: Feature Profile ID
        :param cellular_controller_id: Cellular Controller Feature ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "cellularControllerId": cellular_controller_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-controller/{cellularControllerId}/cellular-profile",
            return_type=str,
            params=params,
            **kw,
        )

    def create_cellular_controller_and_cellular_profile_parcel_association_for_transport_1(
        self, transport_id: str, cellular_controller_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Associate a cellularcontroller feature with a cellularprofile Parcel for transport feature profile

        :param transport_id: Feature Profile ID
        :param cellular_controller_id: Cellular Controller Feature ID
        :param payload: Cellular Profile Parcel Id
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "cellularControllerId": cellular_controller_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-controller/{cellularControllerId}/cellular-profile",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_cellular_controller_associated_cellular_profile_parcel_by_parcel_id_for_transport_1(
        self, transport_id: str, cellular_controller_id: str, cellular_profile_id: str, **kw
    ) -> str:
        """
        Get CellularController feature associated CellularProfile Parcel by cellularProfileId for transport feature profile

        :param transport_id: Feature Profile ID
        :param cellular_controller_id: Cellular Controller Feature ID
        :param cellular_profile_id: Cellular Profile Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "cellularControllerId": cellular_controller_id,
            "cellularProfileId": cellular_profile_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-controller/{cellularControllerId}/cellular-profile/{cellularProfileId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_cellular_controller_and_cellular_profile_parcel_association_for_transport_1(
        self,
        transport_id: str,
        cellular_controller_id: str,
        cellular_profile_id: str,
        payload: Optional[str] = None,
        **kw,
    ) -> str:
        """
        Update a CellularController feature and a CellularProfile Parcel association for transport feature profile

        :param transport_id: Feature Profile ID
        :param cellular_controller_id: Cellular Controller Feature ID
        :param cellular_profile_id: Cellular Profile ID
        :param payload: Cellular Profile Parcel
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "cellularControllerId": cellular_controller_id,
            "cellularProfileId": cellular_profile_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-controller/{cellularControllerId}/cellular-profile/{cellularProfileId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_cellular_controller_and_cellular_profile_association_for_transport_1(
        self, transport_id: str, cellular_controller_id: str, cellular_profile_id: str, **kw
    ):
        """
        Delete a CellularController feature and a CellularProfile Parcel association for transport feature profile

        :param transport_id: Feature Profile ID
        :param cellular_controller_id: Cellular Controller Feature ID
        :param cellular_profile_id: Cellular Profile Parcel ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "cellularControllerId": cellular_controller_id,
            "cellularProfileId": cellular_profile_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-controller/{cellularControllerId}/cellular-profile/{cellularProfileId}",
            params=params,
            **kw,
        )
