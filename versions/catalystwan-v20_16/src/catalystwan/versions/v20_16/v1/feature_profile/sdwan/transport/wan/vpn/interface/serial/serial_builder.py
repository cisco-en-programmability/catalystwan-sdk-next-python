# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .schema.schema_builder import SchemaBuilder


class SerialBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/transport/wan/vpn/interface/serial
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_interface_serial_parcels_for_transport_wan_vpn(
        self, transport_id: str, vpn_id: str, **kw
    ) -> str:
        """
        Get InterfaceSerial Parcels for transport WanVpn Parcel

        :param transport_id: Feature Profile ID
        :param vpn_id: Feature Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/serial",
            return_type=str,
            params=params,
            **kw,
        )

    def create_wan_vpn_interface_serial_parcel_for_transport(
        self, transport_id: str, vpn_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a WanVpn InterfaceSerial parcel for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param payload: Wan Vpn Interface Serial Profile Parcel
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/serial",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_wan_vpn_interface_serial_parcel_by_parcel_id_for_transport(
        self, transport_id: str, vpn_id: str, serial_id: str, **kw
    ) -> str:
        """
        Get WanVpn InterfaceSerial Parcel by serialId for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param serial_id: Interface Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
            "serialId": serial_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/serial/{serialId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_wan_vpn_interface_serial_parcel_for_transport(
        self, transport_id: str, vpn_id: str, serial_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Update a WanVpn InterfaceSerial Parcel for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param serial_id: Interface ID
        :param payload: Wan Vpn Interface Serial Profile Parcel
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
            "serialId": serial_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/serial/{serialId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_wan_vpn_interface_serial_for_transport(
        self, transport_id: str, vpn_id: str, serial_id: str, **kw
    ):
        """
        Delete a  WanVpn InterfaceSerial Parcel for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param serial_id: Interface Parcel ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
            "serialId": serial_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/serial/{serialId}",
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
