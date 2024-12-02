# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .interface.interface_builder import InterfaceBuilder
    from .routing.routing_builder import RoutingBuilder
    from .schema.schema_builder import SchemaBuilder


class VpnBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/service/lan/vpn
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_lan_vpn_profile_parcel_for_service(self, service_id: str, **kw) -> str:
        """
        Get Lan Vpn Profile Parcels for Service feature profile

        :param service_id: Feature Profile ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn",
            return_type=str,
            params=params,
            **kw,
        )

    def create_lan_vpn_profile_parcel_for_service(
        self, service_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a Lan Vpn Profile Parcel for Service feature profile

        :param service_id: Feature Profile ID
        :param payload: Lan Vpn Profile Parcel
        :returns: str
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_lan_vpn_profile_parcel_by_parcel_id_for_service(
        self, service_id: str, vpn_id: str, **kw
    ) -> str:
        """
        Get Lan Vpn Profile Parcel by parcelId for Service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_lan_vpn_profile_parcel_for_service(
        self, service_id: str, vpn_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Update a Lan Vpn Profile Parcel for Service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param payload: Lan Vpn Profile Parcel
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_lan_vpn_profile_parcel_for_service(self, service_id: str, vpn_id: str, **kw):
        """
        Delete a Lan Vpn Profile Parcel for Service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}",
            params=params,
            **kw,
        )

    @property
    def interface(self) -> InterfaceBuilder:
        """
        The interface property
        """
        from .interface.interface_builder import InterfaceBuilder

        return InterfaceBuilder(self._request_adapter)

    @property
    def routing(self) -> RoutingBuilder:
        """
        The routing property
        """
        from .routing.routing_builder import RoutingBuilder

        return RoutingBuilder(self._request_adapter)

    @property
    def schema(self) -> SchemaBuilder:
        """
        The schema property
        """
        from .schema.schema_builder import SchemaBuilder

        return SchemaBuilder(self._request_adapter)
