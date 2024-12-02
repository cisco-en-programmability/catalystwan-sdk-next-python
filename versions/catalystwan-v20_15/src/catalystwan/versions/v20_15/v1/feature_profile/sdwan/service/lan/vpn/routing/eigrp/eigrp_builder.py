# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface


class EigrpBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/eigrp
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_lan_vpn_associated_routing_eigrp_parcels_for_service(
        self, service_id: str, vpn_id: str, **kw
    ) -> str:
        """
        Get LanVpn associated Routing Eigrp Features for service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Feature Feature ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/eigrp",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_lan_vpn_and_routing_eigrp_parcel_association_for_service(self):
        class create_lan_vpn_and_routing_eigrp_parcel_association_for_service_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, service_id: str, vpn_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Associate a lanvpn feature with a routingeigrp Feature for service feature profile

                :param service_id: Feature Profile ID
                :param vpn_id: Lan Vpn Profile Feature ID
                :param payload: Routing Eigrp Profile Feature Id
                :returns: str
                """
                params = {
                    "serviceId": service_id,
                    "vpnId": vpn_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/eigrp",
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

        return create_lan_vpn_and_routing_eigrp_parcel_association_for_service_(
            self._request_adapter
        )

    def get_lan_vpn_associated_routing_eigrp_parcel_by_parcel_id_for_service(
        self, service_id: str, vpn_id: str, eigrp_id: str, **kw
    ) -> str:
        """
        Get LanVpn feature associated RoutingEigrp Feature by eigrpId for service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Profile Feature ID
        :param eigrp_id: Routing Eigrp Feature ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
            "eigrpId": eigrp_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/eigrp/{eigrpId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_lan_vpn_and_routing_eigrp_parcel_association_for_service(self):
        class edit_lan_vpn_and_routing_eigrp_parcel_association_for_service_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                service_id: str,
                vpn_id: str,
                eigrp_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Update a LanVpn feature and a RoutingEigrp Feature association for service feature profile

                :param service_id: Feature Profile ID
                :param vpn_id: Profile Feature ID
                :param eigrp_id: Routing Eigrp ID
                :param payload: Routing Eigrp Profile Feature
                :returns: str
                """
                params = {
                    "serviceId": service_id,
                    "vpnId": vpn_id,
                    "eigrpId": eigrp_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/eigrp/{eigrpId}",
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

        return edit_lan_vpn_and_routing_eigrp_parcel_association_for_service_(
            self._request_adapter
        )

    def delete_lan_vpn_and_routing_eigrp_association_for_service(
        self, service_id: str, vpn_id: str, eigrp_id: str, **kw
    ):
        """
        Delete a LanVpn feature and a RoutingEigrp Feature association for service feature profile

        :param service_id: Feature Profile ID
        :param vpn_id: Profile Feature ID
        :param eigrp_id: Routing Eigrp Feature ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "vpnId": vpn_id,
            "eigrpId": eigrp_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/eigrp/{eigrpId}",
            params=params,
            **kw,
        )
