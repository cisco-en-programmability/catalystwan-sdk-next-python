# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface


class Ipv6Builder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/transport/{transportId}/routing/ospfv3/ipv6
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_routing_ospfv3_ipv6_af_profile_parcel_for_transport(
        self, transport_id: str, **kw
    ) -> str:
        """
        Get all routing OSPFv3 IPv6 address family profile parcels for transport feature profile

        :param transport_id: Feature Profile ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/ospfv3/ipv6",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_routing_ospfv3_ipv6_af_profile_parcel_for_transport(self):
        class create_routing_ospfv3_ipv6_af_profile_parcel_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, transport_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Create a routing OSPFv3 IPv6 address family profile parcel for transport feature profile

                :param transport_id: Feature Profile ID
                :param payload: Routing Ospfv3 IPv6 Address Family Profile Parcel
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/ospfv3/ipv6",
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

        return create_routing_ospfv3_ipv6_af_profile_parcel_for_transport_(
            self._request_adapter
        )

    def get_routing_ospfv3_ipv6_af_profile_parcel_by_parcel_id_for_transport(
        self, transport_id: str, ospfv3_id: str, **kw
    ) -> str:
        """
        Get the routing OSPFv3 IPv6 address family profile parcel by ID for transport feature profile

        :param transport_id: Feature Profile ID
        :param ospfv3_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "ospfv3Id": ospfv3_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/ospfv3/ipv6/{ospfv3Id}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_routing_ospfv3_ipv6_af_profile_parcel_for_transport(self):
        class edit_routing_ospfv3_ipv6_af_profile_parcel_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                transport_id: str,
                ospfv3_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Update a routing OSPFv3 IPv6 address family profile parcel for transport feature profile

                :param transport_id: Feature Profile ID
                :param ospfv3_id: Profile Parcel ID
                :param payload: Routing Ospfv3 IPv6 Address Family Profile Parcel
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                    "ospfv3Id": ospfv3_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/ospfv3/ipv6/{ospfv3Id}",
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

        return edit_routing_ospfv3_ipv6_af_profile_parcel_for_transport_(
            self._request_adapter
        )

    def delete_routing_ospfv3_ipv6_af_profile_parcel_for_transport(
        self, transport_id: str, ospfv3_id: str, **kw
    ):
        """
        Delete the routing OSPFv3 IPv6 address family profile parcel by ID for transport feature profile

        :param transport_id: Feature Profile ID
        :param ospfv3_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "ospfv3Id": ospfv3_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/ospfv3/ipv6/{ospfv3Id}",
            params=params,
            **kw,
        )
