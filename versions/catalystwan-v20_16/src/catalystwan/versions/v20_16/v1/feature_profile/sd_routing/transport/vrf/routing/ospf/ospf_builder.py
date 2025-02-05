# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class OspfBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/ospf
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_transport_vrf_associated_routing_ospf_features_1(
        self, transport_id: str, vrf_id: str, **kw
    ) -> str:
        """
        Get the WAN VRF associated OSPF features for transport feature profile

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
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/ospf",
            return_type=str,
            params=params,
            **kw,
        )

    def create_transport_vrf_and_routing_ospf_association(
        self, transport_id: str, vrf_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Associate an OSPF feature with the WAN VRF feature for transport feature profile

        :param transport_id: Transport Profile ID
        :param vrf_id: VRF Feature ID
        :param payload: OSPF feature ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/ospf",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_vrf_associated_routing_ospf_by_id(
        self, transport_id: str, vrf_id: str, ospf_id: str, **kw
    ) -> str:
        """
        Get the WAN VRF associated OSPF features by feature ID for transport feature profile

        :param transport_id: Transport Profile ID
        :param vrf_id: VRF Feature ID
        :param ospf_id: OSPF Feature ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
            "ospfId": ospf_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/ospf/{ospfId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_transport_vrf_and_routing_ospf_feature_association(
        self, transport_id: str, vrf_id: str, ospf_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Replace the OSPF feature for the WAN VRF feature in transport feature profile

        :param transport_id: Transport Profile ID
        :param vrf_id: VRF Feature ID
        :param ospf_id: Old OSPF Feature ID
        :param payload: New OSPF Feature ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
            "ospfId": ospf_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/ospf/{ospfId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_transport_vrf_and_routing_ospf_association(
        self, transport_id: str, vrf_id: str, ospf_id: str, **kw
    ):
        """
        Delete the VRF and OSPF feature association for transport feature profile

        :param transport_id: Transport Profile ID
        :param vrf_id: VRF Feature ID
        :param ospf_id: OSPF Feature ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
            "ospfId": ospf_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/ospf/{ospfId}",
            params=params,
            **kw,
        )
