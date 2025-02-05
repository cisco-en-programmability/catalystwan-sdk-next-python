# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class OspfBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospf
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_service_vrf_associated_routing_ospf_features(
        self, service_id: str, vrf_id: str, **kw
    ) -> str:
        """
        Get the VRF associated OSPF features for service feature profile

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
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospf",
            return_type=str,
            params=params,
            **kw,
        )

    def create_service_vrf_and_routing_ospf_parcel_association(
        self, service_id: str, vrf_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Associate an OSPF feature with the LAN VRF feature for service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param payload: New OSPF Feature ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospf",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_service_vrf_associated_routing_ospf_feature_by_id(
        self, service_id: str, vrf_id: str, ospf_id: str, **kw
    ) -> str:
        """
        Get the LAN VRF associated OSPF feature by ID for service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param ospf_id: OSPF Feature ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
            "ospfId": ospf_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospf/{ospfId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_service_vrf_and_routing_ospf_feature_association(
        self, service_id: str, vrf_id: str, ospf_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Replace the OSPF feature for LAN VRF feature in service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param ospf_id: Old OSPF Feature ID
        :param payload: New OSPF Feature ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
            "ospfId": ospf_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospf/{ospfId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_service_vrf_and_routing_ospf_association(
        self, service_id: str, vrf_id: str, ospf_id: str, **kw
    ):
        """
        Delete the LAN VRF feature and OSPF feature association in service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param ospf_id: OSPF Feature ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
            "ospfId": ospf_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospf/{ospfId}",
            params=params,
            **kw,
        )
