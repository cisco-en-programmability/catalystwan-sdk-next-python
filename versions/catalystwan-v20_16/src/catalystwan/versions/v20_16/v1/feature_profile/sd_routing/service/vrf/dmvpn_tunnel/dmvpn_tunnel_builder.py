# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class DmvpnTunnelBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/dmvpn-tunnel
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdrouting_service_vrf_dmvpn_tunnel_features(
        self, service_id: str, vrf_id: str, **kw
    ) -> str:
        """
        Get all SD-Routing VRF DMVPN Tunnel features from a specific service feature profile

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
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/dmvpn-tunnel",
            return_type=str,
            params=params,
            **kw,
        )

    def create_sdrouting_service_vrf_dmvpn_tunnel_feature(
        self, service_id: str, vrf_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a SD-Routing VRF DMVPN Tunnel feature from a specific service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param payload: SD-Routing VRF DMVPN Tunnel feature from a specific service feature profile
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/dmvpn-tunnel",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_sdrouting_service_vrf_dmvpn_tunnel_feature(
        self, service_id: str, vrf_id: str, tunnel_id: str, **kw
    ) -> str:
        """
        Get the SD-Routing VRF DMVPN Tunnel feature from a specific service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param tunnel_id: DMVPN Tunnel Interface Feature ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
            "tunnelId": tunnel_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/dmvpn-tunnel/{tunnelId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_sdrouting_service_vrf_dmvpn_tunnel_feature(
        self, service_id: str, vrf_id: str, tunnel_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit the SD-Routing VRF DMVPN Tunnel feature from a specific service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param tunnel_id: DMVPN Tunnel Interface Feature ID
        :param payload: SD-Routing VRF DMVPN Tunnel feature from a specific service feature profile
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
            "tunnelId": tunnel_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/dmvpn-tunnel/{tunnelId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sdrouting_service_vrf_dmvpn_tunnel_feature(
        self, service_id: str, vrf_id: str, tunnel_id: str, **kw
    ):
        """
        Delete the SD-Routing VRF DMVPN Tunnel feature from a specific service feature profile

        :param service_id: Service Profile ID
        :param vrf_id: VRF Feature ID
        :param tunnel_id: DMVPN Tunnel Interface Feature ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "vrfId": vrf_id,
            "tunnelId": tunnel_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/dmvpn-tunnel/{tunnelId}",
            params=params,
            **kw,
        )
