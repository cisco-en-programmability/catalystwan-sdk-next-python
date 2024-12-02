# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface


class OspfBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospf
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_wan_vpn_associated_routing_ospf_parcels_for_transport(
        self, transport_id: str, vpn_id: str, **kw
    ) -> str:
        """
        Get WanVpn associated Routing Ospf Parcels for transport feature profile

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
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospf",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_wan_vpn_and_routing_ospf_parcel_association_for_transport(self):
        class create_wan_vpn_and_routing_ospf_parcel_association_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                transport_id: str,
                vpn_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Associate a wan/vpn parcel with a routing/ospf Parcel for transport feature profile

                :param transport_id: Feature Profile ID
                :param vpn_id: Lan Vpn Profile Parcel ID
                :param payload: Routing Ospf Profile Parcel Id
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                    "vpnId": vpn_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospf",
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

        return create_wan_vpn_and_routing_ospf_parcel_association_for_transport_(
            self._request_adapter
        )

    def get_wan_vpn_associated_routing_ospf_parcel_by_parcel_id_for_transport(
        self, transport_id: str, vpn_id: str, ospf_id: str, **kw
    ) -> str:
        """
        Get WanVpn parcel associated RoutingOspf Parcel by ospfId for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param ospf_id: Routing Ospf Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
            "ospfId": ospf_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospf/{ospfId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_wan_vpn_and_routing_ospf_parcel_association_for_transport(self):
        class edit_wan_vpn_and_routing_ospf_parcel_association_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                transport_id: str,
                vpn_id: str,
                ospf_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Update a WanVpn parcel and a RoutingOspf Parcel association for transport feature profile

                :param transport_id: Feature Profile ID
                :param vpn_id: Profile Parcel ID
                :param ospf_id: Routing Ospf ID
                :param payload: Routing Ospf Profile Parcel
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                    "vpnId": vpn_id,
                    "ospfId": ospf_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospf/{ospfId}",
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

        return edit_wan_vpn_and_routing_ospf_parcel_association_for_transport_(
            self._request_adapter
        )

    def delete_wan_vpn_and_routing_ospf_association_for_transport(
        self, transport_id: str, vpn_id: str, ospf_id: str, **kw
    ):
        """
        Delete a WanVpn parcel and a RoutingOspf Parcel association for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param ospf_id: Routing Ospf Parcel ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
            "ospfId": ospf_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospf/{ospfId}",
            params=params,
            **kw,
        )
