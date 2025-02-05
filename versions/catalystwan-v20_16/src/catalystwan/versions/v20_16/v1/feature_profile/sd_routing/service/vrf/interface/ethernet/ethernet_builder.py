# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .dhcp_server.dhcp_server_builder import DhcpServerBuilder


class EthernetBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdrouting_service_vrf_interface_ethernet_features_for_service(
        self, service_id: str, vrf_id: str, **kw
    ) -> str:
        """
        Get all ethernet interface features from a specific service VRF feature in service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet",
            return_type=str,
            params=params,
            **kw,
        )

    def create_sdrouting_service_vrf_interface_ethernet_feature_for_service(
        self, service_id: str, vrf_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a SD-Routing ethernet interface feature from a specific service VRF feature in service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param payload: SD-Routing ethernet interface feature from a specific service VRF feature
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_sdrouting_service_vrf_interface_ethernet_feature_by_feature_id_for_service(
        self, service_id: str, vrf_id: str, ethernet_id: str, **kw
    ) -> str:
        """
        Get the SD-Routing ethernet interface feature from a specific service VRF feature by feature ID in service feature profile

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
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet/{ethernetId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_sdrouting_service_vrf_interface_ethernet_feature_for_service(
        self, service_id: str, vrf_id: str, ethernet_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit the SD-Routing ethernet interface feature from a specific service VRF feature in service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param ethernet_id: Interface Feature ID
        :param payload: SD-Routing ethernet interface feature from a specific service VRF feature
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
            "ethernetId": ethernet_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet/{ethernetId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sdrouting_service_vrf_interface_ethernet_feature_for_service(
        self, service_id: str, vrf_id: str, ethernet_id: str, **kw
    ):
        """
        Delete the SD-Routing ethernet interface feature from a specific service VRF feature in service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param ethernet_id: Interface Feature ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
            "ethernetId": ethernet_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet/{ethernetId}",
            params=params,
            **kw,
        )

    @property
    def dhcp_server(self) -> DhcpServerBuilder:
        """
        The dhcp-server property
        """
        from .dhcp_server.dhcp_server_builder import DhcpServerBuilder

        return DhcpServerBuilder(self._request_adapter)
