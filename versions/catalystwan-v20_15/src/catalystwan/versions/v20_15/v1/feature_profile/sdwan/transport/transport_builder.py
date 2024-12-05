# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .cellular_controller.cellular_controller_builder import CellularControllerBuilder
    from .cellular_profile.cellular_profile_builder import CellularProfileBuilder
    from .esimcellular_controller.esimcellular_controller_builder import EsimcellularControllerBuilder
    from .esimcellular_profile.esimcellular_profile_builder import EsimcellularProfileBuilder
    from .gps.gps_builder import GpsBuilder
    from .ipv6_tracker.ipv6_tracker_builder import Ipv6TrackerBuilder
    from .ipv6_trackergroup.ipv6_trackergroup_builder import Ipv6TrackergroupBuilder
    from .management.management_builder import ManagementBuilder
    from .routing.routing_builder import RoutingBuilder
    from .t1_e1_controller.t1_e1_controller_builder import T1E1ControllerBuilder
    from .tracker.tracker_builder import TrackerBuilder
    from .trackergroup.trackergroup_builder import TrackergroupBuilder
    from .wan.wan_builder import WanBuilder


class TransportBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/transport
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdwan_transport_feature_profiles(self, offset: Optional[int] = None, limit: Optional[int] = 0, **kw) -> Any:
        """
        Get all SDWAN Feature Profiles with giving Family and profile type

        :param offset: Pagination offset
        :param limit: Pagination limit
        :returns: Any
        """
        params = {
            "offset": offset,
            "limit": limit,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/v1/feature-profile/sdwan/transport", params=params, **kw
        )

    @property
    def create_sdwan_transport_feature_profile(self):
        class create_sdwan_transport_feature_profile_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[str] = None, **kw) -> str:
                """
                Create a SDWAN Transport Feature Profile

                :param payload: SDWAN Feature profile
                :returns: str
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/v1/feature-profile/sdwan/transport", return_type=str, payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return create_sdwan_transport_feature_profile_(self._request_adapter)

    def get_sdwan_transport_feature_profile_by_profile_id(self, transport_id: str, **kw) -> Any:
        """
        Get a SDWAN Transport Feature Profile with transportId

        :param transport_id: Feature Profile Id
        :returns: Any
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/v1/feature-profile/sdwan/transport/{transportId}", params=params, **kw
        )

    @property
    def edit_sdwan_transport_feature_profile(self):
        class edit_sdwan_transport_feature_profile_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, transport_id: str, payload: Optional[str] = None, **kw) -> str:
                """
                Edit a SDWAN Transport Feature Profile

                :param transport_id: Feature Profile Id
                :param payload: SDWAN Feature profile
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}",
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

        return edit_sdwan_transport_feature_profile_(self._request_adapter)

    def delete_sdwan_transport_feature_profile(self, transport_id: str, **kw):
        """
        Delete Feature Profile

        :param transport_id: Transport id
        :returns: None
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "DELETE", "/dataservice/v1/feature-profile/sdwan/transport/{transportId}", params=params, **kw
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
    def esimcellular_controller(self) -> EsimcellularControllerBuilder:
        """
        The esimcellular-controller property
        """
        from .esimcellular_controller.esimcellular_controller_builder import EsimcellularControllerBuilder

        return EsimcellularControllerBuilder(self._request_adapter)

    @property
    def esimcellular_profile(self) -> EsimcellularProfileBuilder:
        """
        The esimcellular-profile property
        """
        from .esimcellular_profile.esimcellular_profile_builder import EsimcellularProfileBuilder

        return EsimcellularProfileBuilder(self._request_adapter)

    @property
    def gps(self) -> GpsBuilder:
        """
        The gps property
        """
        from .gps.gps_builder import GpsBuilder

        return GpsBuilder(self._request_adapter)

    @property
    def ipv6_tracker(self) -> Ipv6TrackerBuilder:
        """
        The ipv6-tracker property
        """
        from .ipv6_tracker.ipv6_tracker_builder import Ipv6TrackerBuilder

        return Ipv6TrackerBuilder(self._request_adapter)

    @property
    def ipv6_trackergroup(self) -> Ipv6TrackergroupBuilder:
        """
        The ipv6-trackergroup property
        """
        from .ipv6_trackergroup.ipv6_trackergroup_builder import Ipv6TrackergroupBuilder

        return Ipv6TrackergroupBuilder(self._request_adapter)

    @property
    def management(self) -> ManagementBuilder:
        """
        The management property
        """
        from .management.management_builder import ManagementBuilder

        return ManagementBuilder(self._request_adapter)

    @property
    def routing(self) -> RoutingBuilder:
        """
        The routing property
        """
        from .routing.routing_builder import RoutingBuilder

        return RoutingBuilder(self._request_adapter)

    @property
    def t1_e1_controller(self) -> T1E1ControllerBuilder:
        """
        The t1-e1-controller property
        """
        from .t1_e1_controller.t1_e1_controller_builder import T1E1ControllerBuilder

        return T1E1ControllerBuilder(self._request_adapter)

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
    def wan(self) -> WanBuilder:
        """
        The wan property
        """
        from .wan.wan_builder import WanBuilder

        return WanBuilder(self._request_adapter)
