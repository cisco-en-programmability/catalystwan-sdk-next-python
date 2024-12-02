# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class GpsBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/transport/{transportId}/cellular-controller/{cellularControllerId}/gps
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_cellular_controller_associated_gps_parcels_for_transport_1(
        self, transport_id: str, cellular_controller_id: str, **kw
    ) -> str:
        """
        Get CellularController associated GPS Features for transport feature profile

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
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-controller/{cellularControllerId}/gps",
            return_type=str,
            params=params,
            **kw,
        )

    def create_cellular_controller_and_gps_parcel_association_for_transport_1(
        self, transport_id: str, cellular_controller_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Associate a cellularcontroller feature with a GPS Parcel for transport feature profile

        :param transport_id: Feature Profile ID
        :param cellular_controller_id: Cellular Controller Feature ID
        :param payload: GPS Profile Parcel Id
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "cellularControllerId": cellular_controller_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-controller/{cellularControllerId}/gps",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_cellular_controller_associated_gps_parcel_by_parcel_id_for_transport_1(
        self, transport_id: str, cellular_controller_id: str, gps_id: str, **kw
    ) -> str:
        """
        Get CellularController feature associated GPS Feature by gpsId for transport feature profile

        :param transport_id: Feature Profile ID
        :param cellular_controller_id: Cellular Controller Feature ID
        :param gps_id: GPS Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "cellularControllerId": cellular_controller_id,
            "gpsId": gps_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-controller/{cellularControllerId}/gps/{gpsId}",
            return_type=str,
            params=params,
            **kw,
        )

    def delete_cellular_controller_and_gps_association_for_transport_1(
        self, transport_id: str, cellular_controller_id: str, gps_id: str, **kw
    ):
        """
        Delete a CellularController feature and a GPS Feature association for transport feature profile

        :param transport_id: Feature Profile ID
        :param cellular_controller_id: Cellular Controller Feature ID
        :param gps_id: GPS Parcel ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "cellularControllerId": cellular_controller_id,
            "gpsId": gps_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-controller/{cellularControllerId}/gps/{gpsId}",
            params=params,
            **kw,
        )
