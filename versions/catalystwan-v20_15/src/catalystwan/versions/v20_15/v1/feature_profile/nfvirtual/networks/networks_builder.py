# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .lan.lan_builder import LanBuilder
    from .ovsnetwork.ovsnetwork_builder import OvsnetworkBuilder
    from .routes.routes_builder import RoutesBuilder
    from .switch.switch_builder import SwitchBuilder
    from .vnf_attributes.vnf_attributes_builder import VnfAttributesBuilder
    from .wan.wan_builder import WanBuilder


class NetworksBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/nfvirtual/networks
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_all_nfvirtual_networks_feature_profiles(
        self, offset: int, limit: int, **kw
    ) -> Any:
        """
        Get all Nfvirtual Feature Profiles

        :param offset: Pagination offset
        :param limit: Pagination limit
        :returns: Any
        """
        params = {
            "offset": offset,
            "limit": limit,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/nfvirtual/networks",
            params=params,
            **kw,
        )

    @property
    def create_nfvirtual_networks_feature_profile(self):
        class create_nfvirtual_networks_feature_profile_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[str] = None, **kw) -> str:
                """
                Create a nfvirtual Networks Feature Profile

                :param payload: Nfvirtual Feature profile
                :returns: str
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/nfvirtual/networks",
                    return_type=str,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return create_nfvirtual_networks_feature_profile_(self._request_adapter)

    def get_nfvirtual_networks_feature_profile_by_profile_id(
        self, network_id: str, details: bool, **kw
    ) -> Any:
        """
        Get a Nfvirtual Networks Feature Profile with networkId

        :param network_id: Feature Profile ID
        :param details: get feature details
        :returns: Any
        """
        params = {
            "networkId": network_id,
            "details": details,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/nfvirtual/networks/{networkId}",
            params=params,
            **kw,
        )

    @property
    def edit_nfvirtual_networks_feature_profile(self):
        class edit_nfvirtual_networks_feature_profile_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, network_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Edit a Nfvirtual Networks Feature Profile

                :param network_id: Feature Profile ID
                :param payload: Nfvirtual Feature profile
                :returns: str
                """
                params = {
                    "networkId": network_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/nfvirtual/networks/{networkId}",
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

        return edit_nfvirtual_networks_feature_profile_(self._request_adapter)

    def delete_nfvirtual_networks_feature_profile(self, network_id: str, **kw):
        """
        Delete a Nfvirtual Networks Feature Profile

        :param network_id: Network id
        :returns: None
        """
        params = {
            "networkId": network_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/nfvirtual/networks/{networkId}",
            params=params,
            **kw,
        )

    @property
    def lan(self) -> LanBuilder:
        """
        The lan property
        """
        from .lan.lan_builder import LanBuilder

        return LanBuilder(self._request_adapter)

    @property
    def ovsnetwork(self) -> OvsnetworkBuilder:
        """
        The ovsnetwork property
        """
        from .ovsnetwork.ovsnetwork_builder import OvsnetworkBuilder

        return OvsnetworkBuilder(self._request_adapter)

    @property
    def routes(self) -> RoutesBuilder:
        """
        The routes property
        """
        from .routes.routes_builder import RoutesBuilder

        return RoutesBuilder(self._request_adapter)

    @property
    def switch(self) -> SwitchBuilder:
        """
        The switch property
        """
        from .switch.switch_builder import SwitchBuilder

        return SwitchBuilder(self._request_adapter)

    @property
    def vnf_attributes(self) -> VnfAttributesBuilder:
        """
        The vnf-attributes property
        """
        from .vnf_attributes.vnf_attributes_builder import VnfAttributesBuilder

        return VnfAttributesBuilder(self._request_adapter)

    @property
    def wan(self) -> WanBuilder:
        """
        The wan property
        """
        from .wan.wan_builder import WanBuilder

        return WanBuilder(self._request_adapter)
