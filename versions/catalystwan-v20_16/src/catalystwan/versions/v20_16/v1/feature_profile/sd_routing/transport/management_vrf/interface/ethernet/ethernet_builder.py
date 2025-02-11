# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class EthernetBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/transport/{transportId}/management-vrf/{vrfId}/interface/ethernet
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdrouting_management_vrf_interface_ethernet_parcels_for_transport_profile(
        self, transport_id: str, vrf_id: str, **kw
    ) -> str:
        """
        Get all  Management Ethernet interface features from a specific management VRF feature in Transport Feature Profile

        :param transport_id: Transport Profile ID
        :param vrf_id: Management VRF Feature ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf/{vrfId}/interface/ethernet",
            return_type=str,
            params=params,
            **kw,
        )

    def create_sdrouting_management_vrf_interface_ethernet_parcel_for_transport_profile(
        self, transport_id: str, vrf_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a SD-Routing Management Ethernet interface feature from a specific management VRF feature in Transport Feature Profile

        :param transport_id: Transport Profile ID
        :param vrf_id: Management VRF Feature ID
        :param payload: SD-Routing Management Ethernet interface feature schema
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf/{vrfId}/interface/ethernet",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_sdrouting_management_vrf_interface_ethernet_parcel_by_parcel_id_for_transport_profile(
        self, transport_id: str, vrf_id: str, ethernet_id: str, **kw
    ) -> str:
        """
        Get the SD-Routing Management Ethernet interface feature from a specific management VRF feature by ethernetId in Transport Feature Profile

        :param transport_id: Transport Profile ID
        :param vrf_id: Management VRF Feature ID
        :param ethernet_id: Management Interface Feature ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
            "ethernetId": ethernet_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf/{vrfId}/interface/ethernet/{ethernetId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_sdrouting_management_vrf_interface_ethernet_parcel_for_transport_profile(
        self, transport_id: str, vrf_id: str, ethernet_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit the SD-Routing Management Ethernet interface feature from a specific management VRF feature in Transport Feature Profile

        :param transport_id: Transport Profile ID
        :param vrf_id: Management VRF Feature ID
        :param ethernet_id: Management Interface Feature ID
        :param payload: SD-Routing Management Ethernet interface feature schema
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
            "ethernetId": ethernet_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf/{vrfId}/interface/ethernet/{ethernetId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sdrouting_management_vrf_interface_ethernet_parcel_for_transport_profile(
        self, transport_id: str, vrf_id: str, ethernet_id: str, **kw
    ):
        """
        Delete the SD-Routing Management Ethernet interface feature from a specific management VRF feature in Transport Feature Profile

        :param transport_id: Transport Profile ID
        :param vrf_id: Management VRF Feature ID
        :param ethernet_id: Management Interface Feature ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
            "ethernetId": ethernet_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf/{vrfId}/interface/ethernet/{ethernetId}",
            params=params,
            **kw,
        )
