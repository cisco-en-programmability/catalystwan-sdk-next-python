# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .cellular_controller.cellular_controller_builder import CellularControllerBuilder
    from .cellular_profile.cellular_profile_builder import CellularProfileBuilder
    from .global_vrf.global_vrf_builder import GlobalVrfBuilder
    from .gps.gps_builder import GpsBuilder
    from .ipv4_acl.ipv4_acl_builder import Ipv4AclBuilder
    from .management_vrf.management_vrf_builder import ManagementVrfBuilder
    from .multicloud_connection.multicloud_connection_builder import MulticloudConnectionBuilder
    from .objecttracker.objecttracker_builder import ObjecttrackerBuilder
    from .objecttrackergroup.objecttrackergroup_builder import ObjecttrackergroupBuilder
    from .route_policy.route_policy_builder import RoutePolicyBuilder
    from .routing.routing_builder import RoutingBuilder
    from .tracker.tracker_builder import TrackerBuilder
    from .trackergroup.trackergroup_builder import TrackergroupBuilder
    from .vrf.vrf_builder import VrfBuilder


class TransportBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/transport
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdrouting_transport_feature_profiles(
        self, offset: Optional[int] = None, limit: Optional[int] = 0, **kw
    ) -> Any:
        """
        Get all SD-Routing Transport Feature Profiles

        :param offset: Pagination offset
        :param limit: Pagination limit
        :returns: Any
        """
        params = {
            "offset": offset,
            "limit": limit,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/v1/feature-profile/sd-routing/transport", params=params, **kw
        )

    def create_sdrouting_transport_feature_profile(
        self, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a SD-Routing Transport Feature Profile

        :param payload: SD-Routing Transport Feature Profile
        :returns: str
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/transport",
            return_type=str,
            payload=payload,
            **kw,
        )

    def get_sdrouting_transport_feature_profile(self, transport_id: str, **kw) -> Any:
        """
        Get a SD-Routing Transport Feature Profile

        :param transport_id: Transport Profile Id
        :returns: Any
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}",
            params=params,
            **kw,
        )

    def edit_sdrouting_transport_feature_profile(
        self, transport_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit a SD-Routing Transport Feature Profile

        :param transport_id: Transport Profile Id
        :param payload: SD-Routing Transport Feature Profile
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sdrouting_transport_feature_profile(self, transport_id: str, **kw):
        """
        Delete a SD-Routing Transport Feature Profile

        :param transport_id: Transport Profile Id
        :returns: None
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}",
            params=params,
            **kw,
        )

    @property
    def cellular_controller(self) -> CellularControllerBuilder:
        """
        The cellular-controller property
        """
        from .cellular_controller.cellular_controller_builder import CellularControllerBuilder

        return CellularControllerBuilder(self._request_adapter)

    @property
    def cellular_profile(self) -> CellularProfileBuilder:
        """
        The cellular-profile property
        """
        from .cellular_profile.cellular_profile_builder import CellularProfileBuilder

        return CellularProfileBuilder(self._request_adapter)

    @property
    def global_vrf(self) -> GlobalVrfBuilder:
        """
        The global-vrf property
        """
        from .global_vrf.global_vrf_builder import GlobalVrfBuilder

        return GlobalVrfBuilder(self._request_adapter)

    @property
    def gps(self) -> GpsBuilder:
        """
        The gps property
        """
        from .gps.gps_builder import GpsBuilder

        return GpsBuilder(self._request_adapter)

    @property
    def ipv4_acl(self) -> Ipv4AclBuilder:
        """
        The ipv4-acl property
        """
        from .ipv4_acl.ipv4_acl_builder import Ipv4AclBuilder

        return Ipv4AclBuilder(self._request_adapter)

    @property
    def management_vrf(self) -> ManagementVrfBuilder:
        """
        The management-vrf property
        """
        from .management_vrf.management_vrf_builder import ManagementVrfBuilder

        return ManagementVrfBuilder(self._request_adapter)

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
    def tracker(self) -> TrackerBuilder:
        """
        The tracker property
        """
        from .tracker.tracker_builder import TrackerBuilder

        return TrackerBuilder(self._request_adapter)

    @property
    def trackergroup(self) -> TrackergroupBuilder:
        """
        The trackergroup property
        """
        from .trackergroup.trackergroup_builder import TrackergroupBuilder

        return TrackergroupBuilder(self._request_adapter)

    @property
    def vrf(self) -> VrfBuilder:
        """
        The vrf property
        """
        from .vrf.vrf_builder import VrfBuilder

        return VrfBuilder(self._request_adapter)
