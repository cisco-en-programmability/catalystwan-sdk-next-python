# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class EthernetBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/interface/ethernet
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdrouting_transport_vrf_interface_ethernet_parcels_for_transport(
        self, transport_id: str, vrf_id: str, **kw
    ) -> str:
        """
        Get all  Ethernet interface features for a specific transport VRF feature in Transport Feature Profile

        :param transport_id: Transport Profile ID
        :param vrf_id: VRF Feature ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/interface/ethernet",
            return_type=str,
            params=params,
            **kw,
        )

    def create_sdrouting_transport_vrf_interface_ethernet_parcel_for_transport(
        self, transport_id: str, vrf_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a SD-Routing Ethernet interface feature from a specific transport VRF feature in Transport Feature Profile

        :param transport_id: Transport Profile ID
        :param vrf_id: VRF Feature ID
        :param payload: SD-Routing Ethernet interface feature from a specific transport VRF feature
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/interface/ethernet",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_sdrouting_transport_vrf_interface_ethernet_parcel_by_parcel_id_for_transport(
        self, transport_id: str, vrf_id: str, ethernet_id: str, **kw
    ) -> str:
        """
        Get the SD-Routing Ethernet interface feature from a specific transport VRF feature by ethernetId in Transport Feature Profile

        :param transport_id: Transport Profile ID
        :param vrf_id: VRF Feature ID
        :param ethernet_id: Interface Feature ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
            "ethernetId": ethernet_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/interface/ethernet/{ethernetId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_sdrouting_transport_vrf_interface_ethernet_parcel_for_transport(
        self, transport_id: str, vrf_id: str, ethernet_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit the SD-Routing Ethernet interface feature from a specific transport VRF feature in Transport Feature Profile

        :param transport_id: Transport Profile ID
        :param vrf_id: VRF Feature ID
        :param ethernet_id: Interface Feature ID
        :param payload: SD-Routing Ethernet interface feature from a specific transport VRF feature
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
            "ethernetId": ethernet_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/interface/ethernet/{ethernetId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sdrouting_transport_vrf_interface_ethernet_parcel_for_transport(
        self, transport_id: str, vrf_id: str, ethernet_id: str, **kw
    ):
        """
        Delete the SD-Routing Ethernet interface feature from a specific transport VRF feature in Transport Feature Profile

        :param transport_id: Transport Profile ID
        :param vrf_id: VRF Feature ID
        :param ethernet_id: Interface Feature ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
            "ethernetId": ethernet_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/interface/ethernet/{ethernetId}",
            params=params,
            **kw,
        )
