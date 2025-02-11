# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class IpsecBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/interface/ipsec
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdrouting_transport_vrf_interface_ipsec_features_for_transport(
        self, transport_id: str, vrf_id: str, **kw
    ) -> str:
        """
        Get all  IPSec interface features in a specific transport VRF from a specific transport feature profile

        :param transport_id: Transport Profile ID
        :param vrf_id: Transport VRF Feature ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/interface/ipsec",
            return_type=str,
            params=params,
            **kw,
        )

    def create_sdrouting_transport_vrf_interface_ipsec_feature_for_transport(
        self, transport_id: str, vrf_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a SD-Routing IPSec interface feature in a specific transport VRF from a specific transport feature profile

        :param transport_id: Transport Profile ID
        :param vrf_id: Transport VRF Feature ID
        :param payload:  IPSec interface feature in a specific transport VRF from a specific transport feature profile
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/interface/ipsec",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_sdrouting_transport_vrf_interface_ipsec_feature_by_feature_id_for_transport(
        self, transport_id: str, vrf_id: str, ipsec_id: str, **kw
    ) -> str:
        """
        Get the SD-Routing IPSec interface feature in a specific transport VRF from a specific transport feature profile

        :param transport_id: Transport Profile ID
        :param vrf_id: Transport VRF Feature ID
        :param ipsec_id: IPSec Interface Feature ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
            "ipsecId": ipsec_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/interface/ipsec/{ipsecId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_sdrouting_transport_vrf_interface_ipsec_feature_for_transport(
        self, transport_id: str, vrf_id: str, ipsec_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit the SD-Routing IPSec interface feature in a specific transport VRF from a specific transport feature profile

        :param transport_id: Transport Profile ID
        :param vrf_id: Transport VRF Feature ID
        :param ipsec_id: IPSec Interface Feature ID
        :param payload:  IPSec interface feature in a specific transport VRF from a specific transport feature profile
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
            "ipsecId": ipsec_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/interface/ipsec/{ipsecId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sdrouting_transport_vrf_interface_ipsec_feature_for_transport(
        self, transport_id: str, vrf_id: str, ipsec_id: str, **kw
    ):
        """
        Delete the SD-Routing IPSec interface feature in a specific transport VRF from a specific transport feature profile

        :param transport_id: Transport Profile ID
        :param vrf_id: Transport VRF feature ID
        :param ipsec_id: IPSec Interface Feature ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
            "ipsecId": ipsec_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/interface/ipsec/{ipsecId}",
            params=params,
            **kw,
        )
