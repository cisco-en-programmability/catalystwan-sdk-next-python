# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class Ipv4Builder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospfv3/ipv4
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_service_vrf_associated_routing_ospfv3_ipv4_features(
        self, service_id: str, vrf_id: str, **kw
    ) -> str:
        """
        Get LAN VRF associated OSPFv3 IPv4 features for service feature profile

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
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospfv3/ipv4",
            return_type=str,
            params=params,
            **kw,
        )

    def create_service_vrf_and_routing_ospfv3_ipv4_feature_association(
        self, service_id: str, vrf_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Associate an OSPFv3 IPv4 feature with the LAN VRF feature for service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param payload: OSPFv3 IPv4 feature ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospfv3/ipv4",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_service_vrf_associated_routing_ospfv3_ipv4_feature_by_id(
        self, service_id: str, vrf_id: str, ospfv3_id: str, **kw
    ) -> str:
        """
        Get the VRF feature associated OSPFv3 IPv4 feature by ID for service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param ospfv3_id: OSPFv3 IPv4 Feature ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
            "ospfv3Id": ospfv3_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospfv3/ipv4/{ospfv3Id}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_service_vrf_and_routing_ospfv3_ipv4_feature_association(
        self, service_id: str, vrf_id: str, ospfv3_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Replace the OSPFv3 IPv4 feature for LAN VRF feature in service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param ospfv3_id: Old OSPFv3 IPv4 Feature ID
        :param payload: Input the new OSPFv3 IPv4 Feature ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
            "ospfv3Id": ospfv3_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospfv3/ipv4/{ospfv3Id}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_service_vrf_and_routing_ospfv3_ipv4_association(
        self, service_id: str, vrf_id: str, ospfv3_id: str, **kw
    ):
        """
        Delete the VRF feature and OSPFv3 IPv4 feature association for service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param ospfv3_id: OSPFv3 IPv4 Feature ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
            "ospfv3Id": ospfv3_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospfv3/ipv4/{ospfv3Id}",
            params=params,
            **kw,
        )
