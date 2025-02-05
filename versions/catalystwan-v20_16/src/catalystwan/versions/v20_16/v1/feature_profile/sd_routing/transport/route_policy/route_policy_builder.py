# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class RoutePolicyBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/transport/{transportId}/route-policy
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdrouting_transport_route_policy_features(self, transport_id: str, **kw) -> str:
        """
        Get all SD-Routing route policy features from a specific transport feature profile

        :param transport_id: Transport Profile ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/route-policy",
            return_type=str,
            params=params,
            **kw,
        )

    def create_sdrouting_transport_route_policy_feature(
        self, transport_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a SD-Routing route policy feature from a specific transport feature profile

        :param transport_id: Transport Profile ID
        :param payload: SD-Routing route policy feature from a specific transport feature profile
        :returns: str
        """
        params = {
            "transportId": transport_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/route-policy",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def get_sdrouting_transport_route_policy_feature(
        self, transport_id: str, route_policy_id: str, **kw
    ) -> str:
        """
        Get the SD-Routing route policy feature from a specific transport feature profile

        :param transport_id: Transport Profile ID
        :param route_policy_id: Route Policy Feature ID
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "routePolicyId": route_policy_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/route-policy/{routePolicyId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_sdrouting_transport_route_policy_feature(
        self, transport_id: str, route_policy_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit the SD-Routing route policy feature from a specific transport feature profile

        :param transport_id: Transport Profile ID
        :param route_policy_id: Route Policy Feature ID
        :param payload: SD-Routing route policy feature from a specific transport feature profile
        :returns: str
        """
        params = {
            "transportId": transport_id,
            "routePolicyId": route_policy_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/route-policy/{routePolicyId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sdrouting_transport_route_policy_feature(
        self, transport_id: str, route_policy_id: str, **kw
    ):
        """
        Delete the SD-Routing route policy feature from a specific transport feature profile

        :param transport_id: Transport Profile ID
        :param route_policy_id: Route Policy Feature ID
        :returns: None
        """
        params = {
            "transportId": transport_id,
            "routePolicyId": route_policy_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/transport/{transportId}/route-policy/{routePolicyId}",
            params=params,
            **kw,
        )
