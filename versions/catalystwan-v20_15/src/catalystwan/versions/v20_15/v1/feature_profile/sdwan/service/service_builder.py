# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .dhcp_server.dhcp_server_builder import DhcpServerBuilder
    from .lan.lan_builder import LanBuilder
    from .routing.routing_builder import RoutingBuilder
    from .switchport.switchport_builder import SwitchportBuilder
    from .tracker.tracker_builder import TrackerBuilder
    from .trackergroup.trackergroup_builder import TrackergroupBuilder
    from .wirelesslan.wirelesslan_builder import WirelesslanBuilder
    from .appqoe.appqoe_builder import AppqoeBuilder


class ServiceBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/service
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdwan_service_feature_profiles(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = 0,
        details: Optional[bool] = False,
        **kw,
    ) -> Any:
        """
        Get all SDWAN Feature Profiles with giving Family and profile type

        :param offset: Pagination offset
        :param limit: Pagination limit
        :param details: get configuration details
        :returns: Any
        """
        params = {
            "offset": offset,
            "limit": limit,
            "details": details,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/v1/feature-profile/sdwan/service", params=params, **kw
        )

    @property
    def create_sdwan_service_feature_profile(self):
        class create_sdwan_service_feature_profile_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[str] = None, **kw) -> str:
                """
                Create a SDWAN Service Feature Profile

                :param payload: SDWAN Feature profile
                :returns: str
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/service",
                    return_type=str,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return create_sdwan_service_feature_profile_(self._request_adapter)

    def get_sdwan_service_feature_profile_by_profile_id(
        self, service_id: str, details: Optional[bool] = False, **kw
    ) -> Any:
        """
        Get a SDWAN Service Feature Profile with serviceId

        :param service_id: Feature Profile Id
        :param details: get feature details
        :returns: Any
        """
        params = {
            "serviceId": service_id,
            "details": details,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}",
            params=params,
            **kw,
        )

    @property
    def edit_sdwan_service_feature_profile(self):
        class edit_sdwan_service_feature_profile_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, service_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Edit a SDWAN Service Feature Profile

                :param service_id: Feature Profile Id
                :param payload: SDWAN Feature profile
                :returns: str
                """
                params = {
                    "serviceId": service_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/service/{serviceId}",
                    return_type=str,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return edit_sdwan_service_feature_profile_(self._request_adapter)

    def delete_sdwan_service_feature_profile(self, service_id: str, **kw):
        """
        Delete Feature Profile

        :param service_id: Service id
        :returns: None
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}",
            params=params,
            **kw,
        )

    @property
    def appqoe(self) -> AppqoeBuilder:
        """
        The appqoe property
        """
        from .appqoe.appqoe_builder import AppqoeBuilder

        return AppqoeBuilder(self._request_adapter)

    @property
    def dhcp_server(self) -> DhcpServerBuilder:
        """
        The dhcp-server property
        """
        from .dhcp_server.dhcp_server_builder import DhcpServerBuilder

        return DhcpServerBuilder(self._request_adapter)

    @property
    def lan(self) -> LanBuilder:
        """
        The lan property
        """
        from .lan.lan_builder import LanBuilder

        return LanBuilder(self._request_adapter)

    @property
    def routing(self) -> RoutingBuilder:
        """
        The routing property
        """
        from .routing.routing_builder import RoutingBuilder

        return RoutingBuilder(self._request_adapter)

    @property
    def switchport(self) -> SwitchportBuilder:
        """
        The switchport property
        """
        from .switchport.switchport_builder import SwitchportBuilder

        return SwitchportBuilder(self._request_adapter)

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
    def wirelesslan(self) -> WirelesslanBuilder:
        """
        The wirelesslan property
        """
        from .wirelesslan.wirelesslan_builder import WirelesslanBuilder

        return WirelesslanBuilder(self._request_adapter)
