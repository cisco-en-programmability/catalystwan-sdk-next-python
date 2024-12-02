# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Type

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .schema.schema_builder import SchemaBuilder


class BgpBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/transport/routing/bgp
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_routing_bgp_profile_parcel_for_transport(
        self, transport_id: str, **kw
    ) -> str:
        """
        Get Routing Bgp Profile Parcels for Transport feature profile

        :param transport_id: Feature Profile ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/bgp",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_routing_bgp_profile_parcel_for_transport(self):
        class create_routing_bgp_profile_parcel_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, transport_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Create a Routing Bgp Profile Parcel for Transport feature profile

                :param transport_id: Feature Profile ID
                :param payload: Routing Bgp Profile Parcel
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/bgp",
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

        return create_routing_bgp_profile_parcel_for_transport_(self._request_adapter)

    def get_routing_bgp_profile_parcel_by_parcel_id_for_transport(
        self, transport_id: str, bgp_id: str, **kw
    ) -> str:
        """
        Get Routing Bgp Profile Parcel by parcelId for Transport feature profile

        :param transport_id: Feature Profile ID
        :param bgp_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "bgpId": bgp_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/bgp/{bgpId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_routing_bgp_profile_parcel_for_transport(self):
        class edit_routing_bgp_profile_parcel_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                transport_id: str,
                bgp_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Update a Routing Bgp Profile Parcel for Transport feature profile

                :param transport_id: Feature Profile ID
                :param bgp_id: Profile Parcel ID
                :param payload: Routing Bgp Profile Parcel
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                    "bgpId": bgp_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/bgp/{bgpId}",
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

        return edit_routing_bgp_profile_parcel_for_transport_(self._request_adapter)

    def delete_routing_bgp_profile_parcel_for_transport(
        self, transport_id: str, bgp_id: str, **kw
    ):
        """
        Delete a Routing Bgp Profile Parcel for Transport feature profile

        :param transport_id: Feature Profile ID
        :param bgp_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "bgpId": bgp_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/bgp/{bgpId}",
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
