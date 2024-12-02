# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class Ipv6Builder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/ospfv3/ipv6
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_transport_vrf_associated_routing_ospfv3_ipv6_features(
        self, transport_id: str, vrf_id: str, **kw
    ) -> str:
        """
        Get the global VRF associated OSPFv3 IPv6 features for transport feature profile

        :param transport_id: Transport Profile ID
        :param vrf_id: Global VRF Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/ospfv3/ipv6",
            return_type=str,
            params=params,
            **kw,
        )

    def create_transport_global_vrf_and_routing_ospfv3_ipv6_parcel_association(
        self, transport_id: str, vrf_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Associate an OSPFv3 IPv6 feature with the global VRF feature for transport feature profile

        :param transport_id: Transport Profile ID
        :param vrf_id: Global VRF Feature ID
        :param payload: New OSPFv3 IPv6 feature ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/ospfv3/ipv6",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_vrf_associated_routing_ospfv3_ipv6_feature_by_id(
        self, transport_id: str, vrf_id: str, ospfv3_id: str, **kw
    ) -> str:
        """
        Get the Global VRF associated OSPFv3 IPv6 feature by ID for transport feature profile

        :param transport_id: Transport Profile ID
        :param vrf_id: Global VRF Parcel ID
        :param ospfv3_id: OSPFv3 IPv6 Feature ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
            "ospfv3Id": ospfv3_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/ospfv3/ipv6/{ospfv3Id}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_transport_global_vrf_and_routing_ospfv3_ipv6_feature_association(
        self, transport_id: str, vrf_id: str, ospfv3_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Replace the OSPFv3 IPv6 feature for the global VRF feature in transport feature profile

        :param transport_id: Transport Profile ID
        :param vrf_id: Global VRF Feature ID
        :param ospfv3_id: Old OSPFv3 IPv6 Feature ID
        :param payload: New OSPFv3 IPv6 Feature ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
            "ospfv3Id": ospfv3_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/ospfv3/ipv6/{ospfv3Id}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_transport_global_vrf_and_routing_ospfv3_ipv6_association(
        self, transport_id: str, vrf_id: str, ospfv3_id: str, **kw
    ):
        """
        Delete the global VRF feature and the OSPFv3 IPv6 feature association for transport feature profile

        :param transport_id: Transport Profile ID
        :param vrf_id: Global VRF Parcel ID
        :param ospfv3_id: OSPFv3 IPv6 Feature ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
            "ospfv3Id": ospfv3_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/ospfv3/ipv6/{ospfv3Id}",
            params=params,
            **kw,
        )
