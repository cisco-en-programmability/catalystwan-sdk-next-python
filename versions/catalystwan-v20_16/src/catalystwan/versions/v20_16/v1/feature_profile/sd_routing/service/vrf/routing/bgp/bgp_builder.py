# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class BgpBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/bgp
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdrouting_service_vrf_bgp_features(self, service_id: str, **kw) -> str:
        """
        Get all SD-Routing LAN BGP features from a specific service feature profile

        :param service_id: Service Profile ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/bgp",
            return_type=str,
            params=params,
            **kw,
        )

    def create_sdrouting_service_vrf_bgp_feature(
        self, service_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a SD-Routing LAN BGP feature from a specific service feature profile

        :param service_id: Service Profile ID
        :param payload: SD-Routing LAN BGP feature from a specific service feature profile
        :returns: str
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/bgp",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_sdrouting_service_vrf_bgp_feature(self, service_id: str, bgp_id: str, **kw) -> str:
        """
        Get the SD-Routing LAN BGP feature from a specific service feature profile

        :param service_id: Service Profile ID
        :param bgp_id: BGP Feature ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "bgpId": bgp_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/bgp/{bgpId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_sdrouting_service_vrf_bgp_feature(
        self, service_id: str, bgp_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit the SD-Routing LAN BGP feature from a specific service feature profile

        :param service_id: Service Profile ID
        :param bgp_id: BGP Feature ID
        :param payload: SD-Routing LAN BGP feature from a specific service feature profile
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "bgpId": bgp_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/bgp/{bgpId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sdrouting_service_vrf_bgp_feature(self, service_id: str, bgp_id: str, **kw):
        """
        Delete the SD-Routing LAN BGP feature from a specific service feature profile

        :param service_id: Service Profile ID
        :param bgp_id: BGP Feature ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "bgpId": bgp_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/bgp/{bgpId}",
            params=params,
            **kw,
        )

    def get_service_vrf_associated_routing_bgp_features(
        self, service_id: str, vrf_id: str, **kw
    ) -> str:
        """
        Get the LAN VRF associated BGP Features for service feature profile

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
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/bgp",
            return_type=str,
            params=params,
            **kw,
        )

    def create_service_vrf_and_routing_bgp_feature_association(
        self, service_id: str, vrf_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Associate a BGP feature with the LAN VRF feature for service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param payload: New BGP feature ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/bgp",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_service_vrf_associated_routing_bgp_parcel_by_parcel_id(
        self, service_id: str, vrf_id: str, bgp_id: str, **kw
    ) -> str:
        """
        Get VRF parcel associated RoutingBGP Parcel by bgpId for service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param bgp_id: BGP Feature ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
            "bgpId": bgp_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/bgp/{bgpId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_service_vrf_and_routing_bgp_feature_association(
        self, service_id: str, vrf_id: str, bgp_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Replace the BGP feature for LAN VRF feature in service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param bgp_id: Old BGP Feature ID
        :param payload: New BGP feature ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
            "bgpId": bgp_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/bgp/{bgpId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_service_vrf_and_routing_bgp_association(
        self, service_id: str, vrf_id: str, bgp_id: str, **kw
    ):
        """
        Delete the LAN VRF feature and BGP feature association for service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param bgp_id: BGP Feature ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
            "bgpId": bgp_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/bgp/{bgpId}",
            params=params,
            **kw,
        )
