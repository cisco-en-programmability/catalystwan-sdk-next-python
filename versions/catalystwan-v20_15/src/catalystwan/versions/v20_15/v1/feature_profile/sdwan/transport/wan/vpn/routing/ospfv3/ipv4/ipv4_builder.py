# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface


class Ipv4Builder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospfv3/ipv4
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_wan_vpn_associated_routing_ospfv3_i_pv4_af_parcels_for_transport(
        self, transport_id: str, vpn_id: str, **kw
    ) -> str:
        """
        Get WAN VPN associated routing OSPFv3 IPv4 address family parcels for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_id: Feature Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospfv3/ipv4",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_wan_vpn_and_routing_ospfv3_ipv4_af_parcel_association_for_transport(self):
        class create_wan_vpn_and_routing_ospfv3_ipv4_af_parcel_association_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, transport_id: str, vpn_id: str, payload: Optional[str] = None, **kw) -> str:
                """
                Associate a WAN VPN parcel with a routing OSPFv3 parcel for transport feature profile

                :param transport_id: Feature Profile ID
                :param vpn_id: WAN Vpn Profile Parcel ID
                :param payload: Routing Ospfv3 IPv4Address Family Profile Parcel Id
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                    "vpnId": vpn_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospfv3/ipv4",
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

        return create_wan_vpn_and_routing_ospfv3_ipv4_af_parcel_association_for_transport_(self._request_adapter)

    def get_wan_vpn_associated_routing_ospfv3_i_pv4_af_parcel_by_parcel_id_for_transport(
        self, transport_id: str, vpn_id: str, ospfv3_id: str, **kw
    ) -> str:
        """
        Get WAN VPN parcel associated OSPFv3 IPv4 parcel by ID for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param ospfv3_id: Routing Ospfv3 IPv4 Address Family Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
            "ospfv3Id": ospfv3_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospfv3/ipv4/{ospfv3Id}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_wan_vpn_and_routing_ospfv3_i_pv4_af_parcel_association_for_transport(self):
        class edit_wan_vpn_and_routing_ospfv3_i_pv4_af_parcel_association_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, transport_id: str, vpn_id: str, ospfv3_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Update a WAN VPN parcel and a routing OSPFv3 parcel association for transport feature profile

                :param transport_id: Feature Profile ID
                :param vpn_id: Profile Parcel ID
                :param ospfv3_id: Routing Ospfv3 IPv4 Address Family parcel ID
                :param payload: Routing Ospfv3 IPv4 Address Family Profile Parcel
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                    "vpnId": vpn_id,
                    "ospfv3Id": ospfv3_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospfv3/ipv4/{ospfv3Id}",
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

        return edit_wan_vpn_and_routing_ospfv3_i_pv4_af_parcel_association_for_transport_(self._request_adapter)

    def delete_wan_vpn_and_routing_ospfv3_i_pv4_association_for_transport(
        self, transport_id: str, vpn_id: str, ospfv3_id: str, **kw
    ):
        """
        Delete a WAN VPN parcel and a routing OSPFv3 parcel association for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param ospfv3_id: Routing Ospfv3 IPv4 Address Family Parcel ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
            "ospfv3Id": ospfv3_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospfv3/ipv4/{ospfv3Id}",
            params=params,
            **kw,
        )
