# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class DhcpServerBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/service/{serviceId}/dhcp-server
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdrouting_dhcp_server_profile_parcels(self, service_id: str, **kw) -> str:
        """
        Get all SD-Routing DHCP Server features in service feature profile

        :param service_id: Service Profile ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/dhcp-server",
            return_type=str,
            params=params,
            **kw,
        )

    def create_sdrouting_dhcp_server_profile_parcel(
        self, service_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a SD-Routing DHCP Server feature in service feature profile

        :param service_id: Service Profile ID
        :param payload: SD-Routing DHCP Server feature in service feature profile
        :returns: str
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/dhcp-server",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_sdrouting_dhcp_server_profile_parcel(
        self, service_id: str, dhcp_server_id: str, **kw
    ) -> str:
        """
        Get a SD-Routing DHCP Server feature in service feature profile

        :param service_id: Service Profile ID
        :param dhcp_server_id: DHCP Server Feature ID
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "dhcpServerId": dhcp_server_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/dhcp-server/{dhcpServerId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_sdrouting_dhcp_server_profile_parcel(
        self, service_id: str, dhcp_server_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit a SD-Routing DHCP Server feature in service feature profile

        :param service_id: Service Profile ID
        :param dhcp_server_id: DHCP Server Feature ID
        :param payload: SD-Routing DHCP Server feature in service feature profile
        :returns: str
        """
        params = {
            "serviceId": service_id,
            "dhcpServerId": dhcp_server_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/dhcp-server/{dhcpServerId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sdrouting_dhcp_server_profile_parcel(
        self, service_id: str, dhcp_server_id: str, **kw
    ):
        """
        Delete a SD-Routing DHCP Server feature in service feature profile

        :param service_id: Service Profile ID
        :param dhcp_server_id: DHCP Server Feature ID
        :returns: None
        """
        params = {
            "serviceId": service_id,
            "dhcpServerId": dhcp_server_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}/dhcp-server/{dhcpServerId}",
            params=params,
            **kw,
        )
