# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class GpsBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/transport/{transportId}/gps
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_gps_profile_parcel_for_transport(self, transport_id: str, **kw) -> str:
        """
        Get GPS Profile Features for Transport feature profile

        :param transport_id: Feature Profile ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/gps",
            return_type=str,
            params=params,
            **kw,
        )

    def create_gps_profile_parcel_for_transport(
        self, transport_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a GPS Profile Feature for Transport feature profile

        :param transport_id: Feature Profile ID
        :param payload: GPS Profile Parcel
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/gps",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_gps_profile_parcel_by_parcel_id_for_transport(
        self, transport_id: str, gps_id: str, **kw
    ) -> str:
        """
        Get GPS Profile Feature by parcelId for Transport feature profile

        :param transport_id: Feature Profile ID
        :param gps_id: GPS Profile Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "gpsId": gps_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/gps/{gpsId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_gps_profile_parcel_for_transport(
        self, transport_id: str, gps_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Update a GPS Profile Feature for Transport feature profile

        :param transport_id: Feature Profile ID
        :param gps_id: GPS Profile Parcel ID
        :param payload: GPS Profile Parcel
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "gpsId": gps_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/gps/{gpsId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_gps_profile_parcel_for_transport(self, transport_id: str, gps_id: str, **kw):
        """
        Delete a GPS Profile Feature for Transport feature profile

        :param transport_id: Feature Profile ID
        :param gps_id: GPS Profile Parcel ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "gpsId": gps_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/gps/{gpsId}",
            params=params,
            **kw,
        )

    def edit_cellular_controller_and_gps_parcel_association_for_transport_1(
        self,
        transport_id: str,
        cellular_controller_id: str,
        gps_id: str,
        payload: Optional[str] = None,
        **kw,
    ) -> str:
        """
        Update a CellularController feature and a GPS Parcel association for transport feature profile

        :param transport_id: Feature Profile ID
        :param cellular_controller_id: Cellular Controller Feature ID
        :param gps_id: GPS Parcel ID
        :param payload: GPS Feature
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "cellularControllerId": cellular_controller_id,
            "gpsId": gps_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/{cellularControllerId}/gps/{gpsId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )
