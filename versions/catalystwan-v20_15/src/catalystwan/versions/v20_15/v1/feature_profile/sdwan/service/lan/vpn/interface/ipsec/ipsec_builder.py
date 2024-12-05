# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Type

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .dhcp_server.dhcp_server_builder import DhcpServerBuilder
    from .schema.schema_builder import SchemaBuilder


class IpsecBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/service/lan/vpn/interface/ipsec
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_list_of_profile_parcels(self, service_id: str, vpn_id: str, **kw) -> str:
        """
        Get InterfaceIpsec Parcels for Service LanVpn Parcel

        :param service_id: Feature Profile ID
        :param vpn_id: Feature Parcel ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ipsec",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_ip_sec_profile_parcel(self):
        class create_ip_sec_profile_parcel_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, service_id: str, vpn_id: str, payload: Optional[str] = None, **kw) -> str:
                """
                Create a LanVpn InterfaceIpsec parcel for service feature profile

                :param service_id: Feature Profile ID
                :param vpn_id: Profile Parcel ID
                :param payload: Wan Vpn Interface Ipsec Profile Parcel
                :returns: str
                """
                params = {
                    "serviceId": service_id,
                    "vpnId": vpn_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ipsec",
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

        return create_ip_sec_profile_parcel_(self._request_adapter)

    def get_profile_parcel_by_parcel_id(self, service_id: str, vpn_id: str, ipsec_id: str, **kw) -> str:
        """
        Get LanVpn InterfaceIpsec Parcel by ethernetId for Service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param ipsec_id: Interface Parcel ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
            "ipsecId": ipsec_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ipsec/{ipsecId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_profile_parcel(self):
        class edit_profile_parcel_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, service_id: str, vpn_id: str, ipsec_id: str, payload: Optional[str] = None, **kw) -> str:
                """
                Update a LanVpn Interface Ipsec Parcel for Service feature profile

                :param service_id: Feature Profile ID
                :param vpn_id: Profile Parcel ID
                :param ipsec_id: Interface ID
                :param payload: Lan Vpn Interface Ipsec Profile Parcel
                :returns: str
                """
                params = {
                    "serviceId": service_id,
                    "vpnId": vpn_id,
                    "ipsecId": ipsec_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ipsec/{ipsecId}",
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

        return edit_profile_parcel_(self._request_adapter)

    def delete_profile_parcel(self, service_id: str, vpn_id: str, ipsec_id: str, **kw):
        """
        Delete a  LanVpn InterfaceIpsec Parcel for Service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param ipsec_id: Interface Parcel ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
            "ipsecId": ipsec_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ipsec/{ipsecId}",
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
    def schema(self) -> SchemaBuilder:
        """
        The schema property
        """
        from .schema.schema_builder import SchemaBuilder

        return SchemaBuilder(self._request_adapter)
