# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Type

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .cellular_profile.cellular_profile_builder import CellularProfileBuilder
    from .gps.gps_builder import GpsBuilder
    from .schema.schema_builder import SchemaBuilder


class CellularControllerBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/transport/cellular-controller
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_cellular_controller_profile_parcel_for_transport(
        self, transport_id: str, **kw
    ) -> str:
        """
        Get Cellular Controller Profile Parcels for Transport feature profile

        :param transport_id: Feature Profile ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_cellular_controller_profile_parcel_for_transport(self):
        class create_cellular_controller_profile_parcel_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, transport_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Create a Cellular Controller Profile Parcel for Transport feature profile

                :param transport_id: Feature Profile ID
                :param payload: Cellular Controller Profile Parcel
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller",
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

        return create_cellular_controller_profile_parcel_for_transport_(
            self._request_adapter
        )

    def get_cellular_controller_profile_parcel_by_parcel_id_for_transport(
        self, transport_id: str, cellular_controller_id: str, **kw
    ) -> str:
        """
        Get Cellular Controller Profile Parcel by parcelId for Transport feature profile

        :param transport_id: Feature Profile ID
        :param cellular_controller_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "cellularControllerId": cellular_controller_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_cellular_controller_profile_parcel_for_transport(self):
        class edit_cellular_controller_profile_parcel_for_transport_:
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
                Update a Cellular Controller Profile Parcel for Transport feature profile

                :param transport_id: Feature Profile ID
                :param cellular_controller_id: Profile Parcel ID
                :param payload: Cellular Controller Profile Parcel
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                    "cellularControllerId": cellular_controller_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}",
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

        return edit_cellular_controller_profile_parcel_for_transport_(
            self._request_adapter
        )

    def delete_cellular_controller_profile_parcel_for_transport(
        self, transport_id: str, cellular_controller_id: str, **kw
    ):
        """
        Delete a Cellular Controller Profile Parcel for Transport feature profile

        :param transport_id: Feature Profile ID
        :param cellular_controller_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "cellularControllerId": cellular_controller_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}",
            params=params,
            **kw,
        )

    @property
    def cellular_profile(self) -> CellularProfileBuilder:
        """
        The cellular-profile property
        """
        from .cellular_profile.cellular_profile_builder import CellularProfileBuilder

        return CellularProfileBuilder(self._request_adapter)

    @property
    def gps(self) -> GpsBuilder:
        """
        The gps property
        """
        from .gps.gps_builder import GpsBuilder

        return GpsBuilder(self._request_adapter)

    @property
    def schema(self) -> SchemaBuilder:
        """
        The schema property
        """
        from .schema.schema_builder import SchemaBuilder

        return SchemaBuilder(self._request_adapter)
