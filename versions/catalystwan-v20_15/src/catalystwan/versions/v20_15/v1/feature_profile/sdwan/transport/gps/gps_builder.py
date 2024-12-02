# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface


class GpsBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/transport/{transportId}/gps
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_gps_profile_parcel_for_transport(self, transport_id: str, **kw) -> str:
        """
        Get Gps Profile Parcels for Transport feature profile

        :param transport_id: Feature Profile ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/gps",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_gps_profile_parcel_for_transport(self):
        class create_gps_profile_parcel_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, transport_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Create a Gps Profile Parcel for Transport feature profile

                :param transport_id: Feature Profile ID
                :param payload: Gps Profile Parcel
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/gps",
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

        return create_gps_profile_parcel_for_transport_(self._request_adapter)

    def get_gps_profile_parcel_by_parcel_id_for_transport(
        self, transport_id: str, gps_id: str, **kw
    ) -> str:
        """
        Get Gps Profile Parcel by parcelId for Transport feature profile

        :param transport_id: Feature Profile ID
        :param gps_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "gpsId": gps_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/gps/{gpsId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_gps_profile_parcel_for_transport(self):
        class edit_gps_profile_parcel_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                transport_id: str,
                gps_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Update a Gps Profile Parcel for Transport feature profile

                :param transport_id: Feature Profile ID
                :param gps_id: Profile Parcel ID
                :param payload: Gps Profile Parcel
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                    "gpsId": gps_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/gps/{gpsId}",
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

        return edit_gps_profile_parcel_for_transport_(self._request_adapter)

    def delete_gps_profile_parcel_for_transport(
        self, transport_id: str, gps_id: str, **kw
    ):
        """
        Delete a Gps Profile Parcel for Transport feature profile

        :param transport_id: Feature Profile ID
        :param gps_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "gpsId": gps_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/gps/{gpsId}",
            params=params,
            **kw,
        )
