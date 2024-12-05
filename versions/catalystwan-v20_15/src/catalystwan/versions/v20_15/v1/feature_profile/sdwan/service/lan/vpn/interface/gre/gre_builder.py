# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Type

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .schema.schema_builder import SchemaBuilder


class GreBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/service/lan/vpn/interface/gre
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_interface_gres_for_service_lan_vpn(self, service_id: str, vpn_id: str, **kw) -> str:
        """
        Get InterfaceGre for service LanVpn

        :param service_id: Feature Profile ID
        :param vpn_id: Vpn ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/gre",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_lan_vpn_interface_gre_for_service(self):
        class create_lan_vpn_interface_gre_for_service_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, service_id: str, vpn_id: str, payload: Optional[str] = None, **kw) -> str:
                """
                Create a LanVpn InterfaceGre for service feature profile

                :param service_id: Feature Profile ID
                :param vpn_id: Vpn ID
                :param payload: Lan Vpn Interface Gre
                :returns: str
                """
                params = {
                    "serviceId": service_id,
                    "vpnId": vpn_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/gre",
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

        return create_lan_vpn_interface_gre_for_service_(self._request_adapter)

    def get_lan_vpn_interface_gre_by_id_for_service(self, service_id: str, vpn_id: str, gre_id: str, **kw) -> str:
        """
        Get LanVpn InterfaceGre by greId for service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Vpn ID
        :param gre_id: Gre ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
            "greId": gre_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/gre/{greId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_lan_vpn_interface_gre_for_service(self):
        class edit_lan_vpn_interface_gre_for_service_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, service_id: str, vpn_id: str, gre_id: str, payload: Optional[str] = None, **kw) -> str:
                """
                Update a LanVpn InterfaceGre Feature for service feature profile

                :param service_id: Feature Profile ID
                :param vpn_id: Vpn ID
                :param gre_id: Interface ID
                :param payload: Lan Vpn Interface Gre
                :returns: str
                """
                params = {
                    "serviceId": service_id,
                    "vpnId": vpn_id,
                    "greId": gre_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/gre/{greId}",
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

        return edit_lan_vpn_interface_gre_for_service_(self._request_adapter)

    def delete_lan_vpn_interface_gre_for_service(self, service_id: str, vpn_id: str, gre_id: str, **kw):
        """
        Delete a  LanVpn InterfaceGre for service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Vpn ID
        :param gre_id: Gre ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
            "greId": gre_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/gre/{greId}",
            params=params,
            **kw,
        )

    @property
    def schema(self) -> SchemaBuilder:
        """
        The schema property
        """
        from .schema.schema_builder import SchemaBuilder

        return SchemaBuilder(self._request_adapter)
