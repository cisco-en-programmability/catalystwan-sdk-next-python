# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .schema.schema_builder import SchemaBuilder
    from .dhcp_server.dhcp_server_builder import DhcpServerBuilder


class SviBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/service/lan/vpn/interface/svi
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_interface_svi_parcels_for_service_lan_vpn(
        self, service_id: str, vpn_id: str, **kw
    ) -> str:
        """
        Get InterfaceSvi Parcels for service LanVpn Parcel

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
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_lan_vpn_interface_svi_parcel_for_service(self):
        class create_lan_vpn_interface_svi_parcel_for_service_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, service_id: str, vpn_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Create a LanVpn InterfaceSvi parcel for service feature profile

                :param service_id: Feature Profile ID
                :param vpn_id: Profile Parcel ID
                :param payload: Lan Vpn Interface Svi Profile Parcel
                :returns: str
                """
                params = {
                    "serviceId": service_id,
                    "vpnId": vpn_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi",
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

        return create_lan_vpn_interface_svi_parcel_for_service_(self._request_adapter)

    def get_lan_vpn_interface_svi_parcel_by_parcel_id_for_service(
        self, service_id: str, vpn_id: str, svi_id: str, **kw
    ) -> str:
        """
        Get LanVpn InterfaceSvi Parcel by sviId for service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param svi_id: Interface Parcel ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
            "sviId": svi_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi/{sviId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_lan_vpn_interface_svi_parcel_for_service(self):
        class edit_lan_vpn_interface_svi_parcel_for_service_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                service_id: str,
                vpn_id: str,
                svi_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Update a LanVpn InterfaceSvi Parcel for service feature profile

                :param service_id: Feature Profile ID
                :param vpn_id: Profile Parcel ID
                :param svi_id: Interface ID
                :param payload: Lan Vpn Interface Svi Profile Parcel
                :returns: str
                """
                params = {
                    "serviceId": service_id,
                    "vpnId": vpn_id,
                    "sviId": svi_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi/{sviId}",
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

        return edit_lan_vpn_interface_svi_parcel_for_service_(self._request_adapter)

    def delete_lan_vpn_interface_svi_for_service(
        self, service_id: str, vpn_id: str, svi_id: str, **kw
    ):
        """
        Delete a  LanVpn InterfaceSvi Parcel for service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param svi_id: Interface Parcel ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
            "sviId": svi_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi/{sviId}",
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
