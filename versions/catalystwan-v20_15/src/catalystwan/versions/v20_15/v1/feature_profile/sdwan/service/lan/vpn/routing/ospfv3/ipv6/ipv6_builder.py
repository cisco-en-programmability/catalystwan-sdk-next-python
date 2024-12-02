# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface


class Ipv6Builder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospfv3/ipv6
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_lan_vpn_associated_routing_ospfv3_i_pv6_parcels_for_service(
        self, service_id: str, vpn_id: str, **kw
    ) -> str:
        """
        Get LanVpn associated IPv6 address family OSPFv3 Parcels for service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Feature Parcel ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospfv3/ipv6",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_lan_vpn_and_routing_ospfv3_i_pv6_parcel_association_for_service(self):
        class create_lan_vpn_and_routing_ospfv3_i_pv6_parcel_association_for_service_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, service_id: str, vpn_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Associate a LAN VPN parcel with a IPv6 address family OSPFv3 Parcel for service feature profile

                :param service_id: Feature Profile ID
                :param vpn_id: Lan Vpn Profile Parcel ID
                :param payload: IPv6 address family OSPFv3 Profile Parcel Id
                :returns: str
                """
                params = {
                    "serviceId": service_id,
                    "vpnId": vpn_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospfv3/ipv6",
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

        return create_lan_vpn_and_routing_ospfv3_i_pv6_parcel_association_for_service_(
            self._request_adapter
        )

    def get_lan_vpn_associated_routing_ospfv3_i_pv6_parcel_by_parcel_id_for_service(
        self, service_id: str, vpn_id: str, ospfv3_id: str, **kw
    ) -> str:
        """
        Get LanVpn parcel associated IPv6 address family OSPFv3 IPv6 Parcel by ospfv3Id for service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param ospfv3_id: IPv6 Address Family OSPFv3 Parcel ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
            "ospfv3Id": ospfv3_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospfv3/ipv6/{ospfv3Id}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_lan_vpn_and_routing_ospfv3_i_pv6_parcel_association_for_service(self):
        class edit_lan_vpn_and_routing_ospfv3_i_pv6_parcel_association_for_service_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                service_id: str,
                vpn_id: str,
                ospfv3_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Update a LAN VPN parcel and a routing OSPFv3 IPv6 Parcel association for service feature profile

                :param service_id: Feature Profile ID
                :param vpn_id: Profile Parcel ID
                :param ospfv3_id: IPv6 address family OSPFv3 ID
                :param payload: IPv6 address family OSPFv3 Profile Parcel
                :returns: str
                """
                params = {
                    "serviceId": service_id,
                    "vpnId": vpn_id,
                    "ospfv3Id": ospfv3_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospfv3/ipv6/{ospfv3Id}",
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

        return edit_lan_vpn_and_routing_ospfv3_i_pv6_parcel_association_for_service_(
            self._request_adapter
        )

    def delete_lan_vpn_and_routing_ospfv3_association_for_service_1(
        self, service_id: str, vpn_id: str, ospfv3_id: str, **kw
    ):
        """
        Delete a LAN VPN parcel and a IPv6 OSPFv3 parcel association for service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param ospfv3_id: IPv6 Address Family OSPFv3 IPv6 Parcel ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
            "ospfv3Id": ospfv3_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospfv3/ipv6/{ospfv3Id}",
            params=params,
            **kw,
        )
