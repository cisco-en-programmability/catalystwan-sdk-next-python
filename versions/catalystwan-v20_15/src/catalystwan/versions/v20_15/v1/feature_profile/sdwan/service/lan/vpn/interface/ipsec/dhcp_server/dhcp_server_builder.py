# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface


class DhcpServerBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ipsec/{ipsecId}/dhcp-server
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_lan_vpn_interface_ipsec_associated_dhcp_server_parcels_for_transport(
        self, service_id: str, vpn_id: str, ipsec_id: str, **kw
    ) -> str:
        """
        Get LanVpnInterfaceIpsec associated DhcpServer Parcels for service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Feature Parcel ID
        :param ipsec_id: Interface Profile Parcel ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
            "ipsecId": ipsec_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ipsec/{ipsecId}/dhcp-server",
            return_type=str,
            params=params,
            **kw,
        )

    def get_lan_vpn_interface_ipsec_associated_dhcp_server_parcel_by_parcel_id_for_transport(
        self, service_id: str, vpn_id: str, ipsec_id: str, dhcp_server_id: str, **kw
    ) -> str:
        """
        Get LanVpnInterfaceIpsec associated DhcpServer Parcel by dhcpServerId for service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param ipsec_id: Interface Profile Parcel ID
        :param dhcp_server_id: DhcpServer Parcel ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
            "ipsecId": ipsec_id,
            "dhcpServerId": dhcp_server_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ipsec/{ipsecId}/dhcp-server/{dhcpServerId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_lan_vpn_interface_ipsec_and_dhcp_server_parcel_association_for_transport(self):
        class edit_lan_vpn_interface_ipsec_and_dhcp_server_parcel_association_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                service_id: str,
                vpn_id: str,
                ipsec_id: str,
                dhcp_server_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Update a LanVpnInterfaceIpsec parcel and a DhcpServer Parcel association for service feature profile

                :param service_id: Feature Profile ID
                :param vpn_id: Profile Parcel ID
                :param ipsec_id: Interface Profile Parcel ID
                :param dhcp_server_id: DhcpServer ID
                :param payload: DhcpServer Profile Parcel
                :returns: str
                """
                params = {
                    "serviceId": service_id,
                    "vpnId": vpn_id,
                    "ipsecId": ipsec_id,
                    "dhcpServerId": dhcp_server_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ipsec/{ipsecId}/dhcp-server/{dhcpServerId}",
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

        return edit_lan_vpn_interface_ipsec_and_dhcp_server_parcel_association_for_transport_(self._request_adapter)

    def delete_lan_vpn_interface_ipsec_and_dhcp_server_association_for_transport(
        self, service_id: str, vpn_id: str, ipsec_id: str, dhcp_server_id: str, **kw
    ):
        """
        Delete a LanVpnInterfaceIpsec and a DhcpServer Parcel association for service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param ipsec_id: Interface Profile Parcel ID
        :param dhcp_server_id: DhcpServer Parcel ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
            "ipsecId": ipsec_id,
            "dhcpServerId": dhcp_server_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ipsec/{ipsecId}/dhcp-server/{dhcpServerId}",
            params=params,
            **kw,
        )

    @property
    def create_lan_vpn_interface_ipsec_and_dhcp_server_parcel_association_for_transport(self):
        class create_lan_vpn_interface_ipsec_and_dhcp_server_parcel_association_for_transport_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, service_id: str, vpn_parcel_id: str, ipsec_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Associate a LanVpnInterfaceIpsec parcel with a DhcpServer Parcel for service feature profile

                :param service_id: Feature Profile ID
                :param vpn_parcel_id: VPN Profile Parcel ID
                :param ipsec_id: Interface Profile Parcel ID
                :param payload: DhcpServer Profile Parcel Id
                :returns: str
                """
                params = {
                    "serviceId": service_id,
                    "vpnParcelId": vpn_parcel_id,
                    "ipsecId": ipsec_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnParcelId}/interface/ipsec/{ipsecId}/dhcp-server",
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

        return create_lan_vpn_interface_ipsec_and_dhcp_server_parcel_association_for_transport_(self._request_adapter)
