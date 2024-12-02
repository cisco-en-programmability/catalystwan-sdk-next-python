# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class BgpBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/routing/bgp
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdrouting_transport_global_vrf_bgp_features(self, transport_id: str, **kw) -> str:
        """
        Get all SD-Routing WAN BGP features for global VRF from a specific transport feature profile

        :param transport_id: Transport Profile ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/routing/bgp",
            return_type=str,
            params=params,
            **kw,
        )

    def create_sdrouting_transport_global_vrf_bgp_feature(
        self, transport_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a SD-Routing WAN BGP feature for global VRF from a specific transport feature profile

        :param transport_id: Transport Profile ID
        :param payload: SD-Routing WAN BGP feature for global VRF from a specific transport feature profile
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/routing/bgp",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_sdrouting_transport_global_vrf_bgp_feature(
        self, transport_id: str, bgp_id: str, **kw
    ) -> str:
        """
        Get the SD-Routing WAN BGP feature for global VRF from a specific transport feature profile

        :param transport_id: Transport Profile ID
        :param bgp_id: BGP Feature ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "bgpId": bgp_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/routing/bgp/{bgpId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_sdrouting_transport_global_vrf_bgp_feature(
        self, transport_id: str, bgp_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit the SD-Routing WAN BGP feature for global VRF from a specific transport feature profile

        :param transport_id: Transport Profile ID
        :param bgp_id: BGP Feature ID
        :param payload: SD-Routing WAN BGP feature for global VRF from a specific transport feature profile
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "bgpId": bgp_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/routing/bgp/{bgpId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sdrouting_transport_global_vrf_bgp_feature(
        self, transport_id: str, bgp_id: str, **kw
    ):
        """
        Delete the SD-Routing WAN BGP feature for global VRF from a specific transport feature profile

        :param transport_id: Transport Profile ID
        :param bgp_id: BGP Feature ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "bgpId": bgp_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/routing/bgp/{bgpId}",
            params=params,
            **kw,
        )

    def get_transport_vrf_associated_routing_bgp_features(
        self, transport_id: str, vrf_id: str, **kw
    ) -> str:
        """
        Get the global VRF associated BGP features for transport feature profile

        :param transport_id: Transport Profile ID
        :param vrf_id: Global VRF Feature ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/bgp",
            return_type=str,
            params=params,
            **kw,
        )

    def create_transport_global_vrf_and_routing_bgp_feature_association(
        self, transport_id: str, vrf_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Associate a BGP feature with the global VRF feature for transport feature profile

        :param transport_id: Transport Profile ID
        :param vrf_id: Global VRF Feature ID
        :param payload: New BGP Feature ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/bgp",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_vrf_associated_routing_bgp_feature_by_id(
        self, transport_id: str, vrf_id: str, bgp_id: str, **kw
    ) -> str:
        """
        Get Global VRF parcel associated BGP feature by ID for transport feature profile

        :param transport_id: Transport Profile ID
        :param vrf_id: Global VRF Feature ID
        :param bgp_id: BGP Feature ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
            "bgpId": bgp_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/bgp/{bgpId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_transport_global_vrf_and_routing_bgp_feature_association(
        self, transport_id: str, vrf_id: str, bgp_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Replace the BGP feature for the global VRF feature in transport feature profile

        :param transport_id: Transport Profile ID
        :param vrf_id: Global VRF Feature ID
        :param bgp_id: BGP Feature ID
        :param payload: New BGP feature ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
            "bgpId": bgp_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/bgp/{bgpId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_transport_global_vrf_and_routing_bgp_association(
        self, transport_id: str, vrf_id: str, bgp_id: str, **kw
    ):
        """
        Delete the global VRF and BGP feature association for transport feature profile

        :param transport_id: Transport Profile ID
        :param vrf_id: Global VRF Feature ID
        :param bgp_id: BGP Feature ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "vrfId": vrf_id,
            "bgpId": bgp_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/bgp/{bgpId}",
            params=params,
            **kw,
        )
