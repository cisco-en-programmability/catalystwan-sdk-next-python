# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface


class GpsBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/gps
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_cellular_controller_associated_gps_parcels_for_transport(
        self, transport_id: str, cellular_controller_id: str, **kw
    ) -> str:
        """
        Get CellularController associated Gps Parcels for transport feature profile

        :param transport_id: Feature Profile ID
        :param cellular_controller_id: Feature Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "cellularControllerId": cellular_controller_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/gps",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_cellular_controller_and_gps_parcel_association_for_transport(self):
        class create_cellular_controller_and_gps_parcel_association_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                transport_id: str,
                cellular_controller_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Associate a cellularcontroller parcel with a gps Parcel for transport feature profile

                :param transport_id: Feature Profile ID
                :param cellular_controller_id: Cellular Controller Profile Parcel ID
                :param payload: Gps Profile Parcel Id
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                    "cellularControllerId": cellular_controller_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/gps",
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

        return create_cellular_controller_and_gps_parcel_association_for_transport_(
            self._request_adapter
        )

    def get_cellular_controller_associated_gps_parcel_by_parcel_id_for_transport(
        self, transport_id: str, cellular_controller_id: str, gps_id: str, **kw
    ) -> str:
        """
        Get CellularController parcel associated Gps Parcel by gpsId for transport feature profile

        :param transport_id: Feature Profile ID
        :param cellular_controller_id: Profile Parcel ID
        :param gps_id: Gps Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "cellularControllerId": cellular_controller_id,
            "gpsId": gps_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/gps/{gpsId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_cellular_controller_and_gps_parcel_association_for_transport(self):
        class edit_cellular_controller_and_gps_parcel_association_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                transport_id: str,
                cellular_controller_id: str,
                gps_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Update a CellularController parcel and a Gps Parcel association for transport feature profile

                :param transport_id: Feature Profile ID
                :param cellular_controller_id: Profile Parcel ID
                :param gps_id: Gps ID
                :param payload: Gps Profile Parcel
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                    "cellularControllerId": cellular_controller_id,
                    "gpsId": gps_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/gps/{gpsId}",
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

        return edit_cellular_controller_and_gps_parcel_association_for_transport_(
            self._request_adapter
        )

    def delete_cellular_controller_and_gps_association_for_transport(
        self, transport_id: str, cellular_controller_id: str, gps_id: str, **kw
    ):
        """
        Delete a CellularController parcel and a Gps Parcel association for transport feature profile

        :param transport_id: Feature Profile ID
        :param cellular_controller_id: Profile Parcel ID
        :param gps_id: Gps Parcel ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "cellularControllerId": cellular_controller_id,
            "gpsId": gps_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/gps/{gpsId}",
            params=params,
            **kw,
        )
