# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .schema.schema_builder import SchemaBuilder


class T1E1ControllerBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/transport/t1-e1-controller
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_t1e1controller_profile_parcel_for_transport(
        self, transport_id: str, **kw
    ) -> str:
        """
        Get T1e1controller Profile Parcels for Transport feature profile

        :param transport_id: Feature Profile ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/t1-e1-controller",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_t1e1controller_profile_parcel_for_transport(self):
        class create_t1e1controller_profile_parcel_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, transport_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Create a T1e1controller Profile Parcel for Transport feature profile

                :param transport_id: Feature Profile ID
                :param payload: T1e1controller Profile Parcel
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/t1-e1-controller",
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

        return create_t1e1controller_profile_parcel_for_transport_(
            self._request_adapter
        )

    def get_t1e1controller_profile_parcel_by_parcel_id_for_transport(
        self, transport_id: str, t1e1controller_id: str, **kw
    ) -> str:
        """
        Get T1e1controller Profile Parcel by parcelId for Transport feature profile

        :param transport_id: Feature Profile ID
        :param t1e1controller_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "t1e1controllerId": t1e1controller_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/t1-e1-controller/{t1e1controllerId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_t1e1controller_profile_parcel_for_transport(self):
        class edit_t1e1controller_profile_parcel_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                transport_id: str,
                t1e1controller_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Update a T1e1controller Profile Parcel for Transport feature profile

                :param transport_id: Feature Profile ID
                :param t1e1controller_id: Profile Parcel ID
                :param payload: T1e1controller Profile Parcel
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                    "t1e1controllerId": t1e1controller_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/t1-e1-controller/{t1e1controllerId}",
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

        return edit_t1e1controller_profile_parcel_for_transport_(self._request_adapter)

    def delete_t1e1controller_profile_parcel_for_transport(
        self, transport_id: str, t1e1controller_id: str, **kw
    ):
        """
        Delete a T1e1controller Profile Parcel for Transport feature profile

        :param transport_id: Feature Profile ID
        :param t1e1controller_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "t1e1controllerId": t1e1controller_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/t1-e1-controller/{t1e1controllerId}",
            params=params,
            **kw,
        )

    @property
    def schema(self) -> SchemaBuilder:
        """
        The schema property
        """
        from .schema.schema_builder import SchemaBuilder

        return SchemaBuilder(self._request_adapter)
