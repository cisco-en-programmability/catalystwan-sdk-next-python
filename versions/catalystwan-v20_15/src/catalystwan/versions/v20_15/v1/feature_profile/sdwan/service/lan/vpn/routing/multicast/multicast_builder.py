# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface


class MulticastBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/multicast
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_lan_vpn_associated_routing_multicast_parcels_for_service(
        self, service_id: str, vpn_id: str, **kw
    ) -> str:
        """
        Get LanVpn associated Routing Multicast Parcels for service feature profile

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
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/multicast",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_lan_vpn_and_routing_multicast_parcel_association_for_service(self):
        class create_lan_vpn_and_routing_multicast_parcel_association_for_service_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, service_id: str, vpn_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Associate a lanvpn parcel with a routingmulticast Parcel for service feature profile

                :param service_id: Feature Profile ID
                :param vpn_id: Lan Vpn Profile Parcel ID
                :param payload: Routing Multicast Profile Parcel Id
                :returns: str
                """
                params = {
                    "serviceId": service_id,
                    "vpnId": vpn_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/multicast",
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

        return create_lan_vpn_and_routing_multicast_parcel_association_for_service_(
            self._request_adapter
        )

    def get_lan_vpn_associated_routing_multicast_parcel_by_parcel_id_for_service(
        self, service_id: str, vpn_id: str, multicast_id: str, **kw
    ) -> str:
        """
        Get LanVpn parcel associated RoutingMulticast Parcel by multicastId for service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param multicast_id: Routing Multicast Parcel ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
            "multicastId": multicast_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/multicast/{multicastId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_lan_vpn_and_routing_multicast_parcel_association_for_service(self):
        class edit_lan_vpn_and_routing_multicast_parcel_association_for_service_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                service_id: str,
                vpn_id: str,
                multicast_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Update a LanVpn parcel and a RoutingMulticast Parcel association for service feature profile

                :param service_id: Feature Profile ID
                :param vpn_id: Profile Parcel ID
                :param multicast_id: Routing Multicast ID
                :param payload: Routing Multicast Profile Parcel
                :returns: str
                """
                params = {
                    "serviceId": service_id,
                    "vpnId": vpn_id,
                    "multicastId": multicast_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/multicast/{multicastId}",
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

        return edit_lan_vpn_and_routing_multicast_parcel_association_for_service_(
            self._request_adapter
        )

    def delete_lan_vpn_and_routing_multicast_association_for_service(
        self, service_id: str, vpn_id: str, multicast_id: str, **kw
    ):
        """
        Delete a LanVpn parcel and a RoutingMulticast Parcel association for service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Profile Parcel ID
        :param multicast_id: Routing Multicast Parcel ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
            "multicastId": multicast_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/multicast/{multicastId}",
            params=params,
            **kw,
        )
