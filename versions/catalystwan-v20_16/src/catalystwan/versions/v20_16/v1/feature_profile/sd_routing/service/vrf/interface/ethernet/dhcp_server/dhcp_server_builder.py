# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class DhcpServerBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet/{ethernetId}/dhcp-server
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_vrf_interface_ethernet_associated_dhcp_server_parcels_for_service(
        self, service_id: str, vrf_id: str, ethernet_id: str, **kw
    ) -> str:
        """
        Get the ethernet interface feature associated DHCP server feature in service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param ethernet_id: Interface Feature ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
            "ethernetId": ethernet_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet/{ethernetId}/dhcp-server",
            return_type=str,
            params=params,
            **kw,
        )

    def create_vrf_interface_ethernet_and_dhcp_server_parcel_association_for_service(
        self, service_id: str, vrf_id: str, ethernet_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Associate a SD-Routing ethernet interface feature with a DHCP server feature for service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param ethernet_id: Interface Feature ID
        :param payload: SD-Routing DHCP Server feature for VRF Interface in service feature profile
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
            "ethernetId": ethernet_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet/{ethernetId}/dhcp-server",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_vrf_interface_ethernet_associated_dhcp_server_parcel_by_feature_id_for_service(
        self, service_id: str, vrf_id: str, ethernet_id: str, dhcp_server_id: str, **kw
    ) -> str:
        """
        Get the LAN ethernet interface feature associated DHCP server feature in service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param ethernet_id: Interface Feature ID
        :param dhcp_server_id: DHCP Server Feature ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
            "ethernetId": ethernet_id,
            "dhcpServerId": dhcp_server_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet/{ethernetId}/dhcp-server/{dhcpServerId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_vrf_interface_ethernet_and_dhcp_server_parcel_association_for_service(
        self,
        service_id: str,
        vrf_id: str,
        ethernet_id: str,
        dhcp_server_id: str,
        payload: Optional[str] = None,
        **kw,
    ) -> str:
        """
        Update a SD-Routing LAN ethernet interface feature and a DHCP server feature association for service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param ethernet_id: Interface Feature ID
        :param dhcp_server_id: DHCP Server Feature ID
        :param payload: SD-Routing DHCP Server feature for VRF Interface in service feature profile
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
            "ethernetId": ethernet_id,
            "dhcpServerId": dhcp_server_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet/{ethernetId}/dhcp-server/{dhcpServerId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_vrf_interface_ethernet_and_dhcp_server_association_for_service(
        self, service_id: str, vrf_id: str, ethernet_id: str, dhcp_server_id: str, **kw
    ):
        """
        Delete a LAN ethernet interface feature and a DHCP server feature association for service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param ethernet_id: Interface Feature ID
        :param dhcp_server_id: DHCP Server Feature ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
            "ethernetId": ethernet_id,
            "dhcpServerId": dhcp_server_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet/{ethernetId}/dhcp-server/{dhcpServerId}",
            params=params,
            **kw,
        )
