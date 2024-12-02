# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface


class CellularProfileBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/cellular-profile
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_cellular_controller_associated_cellular_profile_parcels_for_transport(
        self, transport_id: str, cellular_controller_id: str, **kw
    ) -> str:
        """
        Get CellularController associated Cellular Profile Parcels for transport feature profile

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
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/cellular-profile",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_cellular_controller_and_cellular_profile_parcel_association_for_transport(
        self,
    ):
        class create_cellular_controller_and_cellular_profile_parcel_association_for_transport_:
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
                Associate a cellularcontroller parcel with a cellularprofile Parcel for transport feature profile

                :param transport_id: Feature Profile ID
                :param cellular_controller_id: Cellular Controller Profile Parcel ID
                :param payload: Cellular Profile Profile Parcel Id
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                    "cellularControllerId": cellular_controller_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/cellular-profile",
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

        return create_cellular_controller_and_cellular_profile_parcel_association_for_transport_(
            self._request_adapter
        )

    def get_cellular_controller_associated_cellular_profile_parcel_by_parcel_id_for_transport(
        self,
        transport_id: str,
        cellular_controller_id: str,
        cellular_profile_id: str,
        **kw,
    ) -> str:
        """
        Get CellularController parcel associated CellularProfile Parcel by cellularProfileId for transport feature profile

        :param transport_id: Feature Profile ID
        :param cellular_controller_id: Profile Parcel ID
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
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/cellular-profile/{cellularProfileId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_cellular_controller_and_cellular_profile_parcel_association_for_transport(
        self,
    ):
        class edit_cellular_controller_and_cellular_profile_parcel_association_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                transport_id: str,
                cellular_controller_id: str,
                cellular_profile_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Update a CellularController parcel and a CellularProfile Parcel association for transport feature profile

                :param transport_id: Feature Profile ID
                :param cellular_controller_id: Profile Parcel ID
                :param cellular_profile_id: Cellular Profile ID
                :param payload: Cellular Profile Profile Parcel
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                    "cellularControllerId": cellular_controller_id,
                    "cellularProfileId": cellular_profile_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/cellular-profile/{cellularProfileId}",
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

        return edit_cellular_controller_and_cellular_profile_parcel_association_for_transport_(
            self._request_adapter
        )

    def delete_cellular_controller_and_cellular_profile_association_for_transport(
        self,
        transport_id: str,
        cellular_controller_id: str,
        cellular_profile_id: str,
        **kw,
    ):
        """
        Delete a CellularController parcel and a CellularProfile Parcel association for transport feature profile

        :param transport_id: Feature Profile ID
        :param cellular_controller_id: Profile Parcel ID
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
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/cellular-profile/{cellularProfileId}",
            params=params,
            **kw,
        )
