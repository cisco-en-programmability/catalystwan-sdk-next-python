# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .dhcp_server.dhcp_server_builder import DhcpServerBuilder
    from .ipsec_profile.ipsec_profile_builder import IpsecProfileBuilder
    from .ipv4_acl.ipv4_acl_builder import Ipv4AclBuilder
    from .multicloud_connection.multicloud_connection_builder import MulticloudConnectionBuilder
    from .objecttracker.objecttracker_builder import ObjecttrackerBuilder
    from .objecttrackergroup.objecttrackergroup_builder import ObjecttrackergroupBuilder
    from .route_policy.route_policy_builder import RoutePolicyBuilder
    from .routing.routing_builder import RoutingBuilder
    from .vrf.vrf_builder import VrfBuilder


class ServiceBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/service
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sd_routing_service_feature_profiles(
        self, offset: Optional[int] = None, limit: Optional[int] = 0, **kw
    ) -> Any:
        """
        Get all SD-Routing Service Feature Profiles

        :param offset: Pagination offset
        :param limit: Pagination limit
        :returns: Any
        """
        params = {
            "offset": offset,
            "limit": limit,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/v1/feature-profile/sd-routing/service", params=params, **kw
        )

    def create_sd_routing_service_feature_profile(self, payload: Optional[str] = None, **kw) -> str:
        """
        Create a SD-Routing Service Feature Profile

        :param payload: SD-Routing Service Feature Profile
        :returns: str
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/service",
            return_type=str,
            payload=payload,
            **kw,
        )

    def get_sd_routing_service_feature_profile(self, service_id: str, **kw) -> Any:
        """
        Get a SD-Routing Service Feature Profile

        :param service_id: Service Profile Id
        :returns: Any
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}",
            params=params,
            **kw,
        )

    def edit_sd_routing_service_feature_profile(
        self, service_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit a SD-Routing Service Feature Profile

        :param service_id: Service Profile Id
        :param payload: SD-Routing Service Feature Profile
        :returns: str
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sd_routing_service_feature_profile(self, service_id: str, **kw):
        """
        Delete a SD-Routing Service Feature Profile

        :param service_id: Service Profile Id
        :returns: None
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}",
            params=params,
            **kw,
        )

    @property
    def dhcp_server(self) -> DhcpServerBuilder:
        """
        The dhcp-server property
        """
        from .dhcp_server.dhcp_server_builder import DhcpServerBuilder

        return DhcpServerBuilder(self._request_adapter)

    @property
    def ipsec_profile(self) -> IpsecProfileBuilder:
        """
        The ipsec-profile property
        """
        from .ipsec_profile.ipsec_profile_builder import IpsecProfileBuilder

        return IpsecProfileBuilder(self._request_adapter)

    @property
    def ipv4_acl(self) -> Ipv4AclBuilder:
        """
        The ipv4-acl property
        """
        from .ipv4_acl.ipv4_acl_builder import Ipv4AclBuilder

        return Ipv4AclBuilder(self._request_adapter)

    @property
    def multicloud_connection(self) -> MulticloudConnectionBuilder:
        """
        The multicloud-connection property
        """
        from .multicloud_connection.multicloud_connection_builder import MulticloudConnectionBuilder

        return MulticloudConnectionBuilder(self._request_adapter)

    @property
    def objecttracker(self) -> ObjecttrackerBuilder:
        """
        The objecttracker property
        """
        from .objecttracker.objecttracker_builder import ObjecttrackerBuilder

        return ObjecttrackerBuilder(self._request_adapter)

    @property
    def objecttrackergroup(self) -> ObjecttrackergroupBuilder:
        """
        The objecttrackergroup property
        """
        from .objecttrackergroup.objecttrackergroup_builder import ObjecttrackergroupBuilder

        return ObjecttrackergroupBuilder(self._request_adapter)

    @property
    def route_policy(self) -> RoutePolicyBuilder:
        """
        The route-policy property
        """
        from .route_policy.route_policy_builder import RoutePolicyBuilder

        return RoutePolicyBuilder(self._request_adapter)

    @property
    def routing(self) -> RoutingBuilder:
        """
        The routing property
        """
        from .routing.routing_builder import RoutingBuilder

        return RoutingBuilder(self._request_adapter)

    @property
    def vrf(self) -> VrfBuilder:
        """
        The vrf property
        """
        from .vrf.vrf_builder import VrfBuilder

        return VrfBuilder(self._request_adapter)
