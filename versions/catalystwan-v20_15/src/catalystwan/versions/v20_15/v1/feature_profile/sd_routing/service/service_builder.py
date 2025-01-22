# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .multicloud_connection.multicloud_connection_builder import MulticloudConnectionBuilder


class ServiceBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/service
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sd_routing_service_feature_profiles(
        self, offset: Optional[int] = None, limit: Optional[int] = 0, **kw
    ) -> Any:
        """
        Get all SD-Routing Service Feature Profiles

        :param offset: Pagination offset
        :param limit: Pagination limit
        :returns: Any
        """
        params = {
            "offset": offset,
            "limit": limit,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/v1/feature-profile/sd-routing/service", params=params, **kw
        )

    def create_sd_routing_service_feature_profile(self, payload: Optional[str] = None, **kw) -> str:
        """
        Create a SD-Routing Service Feature Profile

        :param payload: SD-Routing Service Feature Profile
        :returns: str
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/service",
            return_type=str,
            payload=payload,
            **kw,
        )

    def get_sd_routing_service_feature_profile(self, service_id: str, **kw) -> Any:
        """
        Get a SD-Routing Service Feature Profile

        :param service_id: Feature Profile Id
        :returns: Any
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}",
            params=params,
            **kw,
        )

    def edit_sd_routing_service_feature_profile(
        self, service_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit a SD-Routing Service Feature Profile

        :param service_id: Feature Profile Id
        :param payload: SD-Routing Service Feature Profile
        :returns: str
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sd_routing_service_feature_profile(self, service_id: str, **kw):
        """
        Delete a SD-Routing Service Feature Profile

        :param service_id: Service id
        :returns: None
        """
        params = {
            "serviceId": service_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/service/{serviceId}",
            params=params,
            **kw,
        )

    @property
    def multicloud_connection(self) -> MulticloudConnectionBuilder:
        """
        The multicloud-connection property
        """
        from .multicloud_connection.multicloud_connection_builder import MulticloudConnectionBuilder

        return MulticloudConnectionBuilder(self._request_adapter)
