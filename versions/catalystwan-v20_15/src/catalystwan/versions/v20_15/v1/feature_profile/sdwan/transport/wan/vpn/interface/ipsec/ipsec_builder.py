# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .schema.schema_builder import SchemaBuilder
    from .tracker.tracker_builder import TrackerBuilder


class IpsecBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/transport/wan/vpn/interface/ipsec
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_list_of_profile_parcels_1(
        self, transport_id: str, vpn_id: str, **kw
    ) -> str:
        """
        Get InterfaceIpsec Parcels for transport WanVpn Parcel

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
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ipsec",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_ip_sec_profile_parcel_1(self):
        class create_ip_sec_profile_parcel_1_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                transport_id: str,
                vpn_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Create a WanVpn InterfaceIpsec parcel for transport feature profile

                :param transport_id: Feature Profile ID
                :param vpn_id: Profile Parcel ID
                :param payload: Wan Vpn Interface Ethernet Profile Parcel
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                    "vpnId": vpn_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ipsec",
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

        return create_ip_sec_profile_parcel_1_(self._request_adapter)

    def get_profile_parcel_by_parcel_id_1(
        self, transport_id: str, vpn_id: str, ipsec_id: str, **kw
    ) -> str:
        """
        Get WanVpn InterfaceIpsec Parcel by ethernetId for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param ipsec_id: Interface Parcel ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
            "ipsecId": ipsec_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ipsec/{ipsecId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_profile_parcel_1(self):
        class edit_profile_parcel_1_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                transport_id: str,
                vpn_id: str,
                ipsec_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Update a WanVpn InterfaceIpsec Parcel for transport feature profile

                :param transport_id: Feature Profile ID
                :param vpn_id: Profile Parcel ID
                :param ipsec_id: Interface ID
                :param payload: Wan Vpn Interface Ipsec Profile Parcel
                :returns: str
                """
                params = {
                    "transportId": transport_id,
                    "vpnId": vpn_id,
                    "ipsecId": ipsec_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ipsec/{ipsecId}",
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

        return edit_profile_parcel_1_(self._request_adapter)

    def delete_profile_parcel_1(
        self, transport_id: str, vpn_id: str, ipsec_id: str, **kw
    ):
        """
        Delete a  WanVpn InterfaceIpsec Parcel for transport feature profile

        :param transport_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param ipsec_id: Interface Parcel ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "vpnId": vpn_id,
            "ipsecId": ipsec_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ipsec/{ipsecId}",
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

    @property
    def tracker(self) -> TrackerBuilder:
        """
        The tracker property
        """
        from .tracker.tracker_builder import TrackerBuilder

        return TrackerBuilder(self._request_adapter)
