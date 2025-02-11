# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .cisco.cisco_builder import CiscoBuilder


class SseBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/sse
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sd_routing_sse_feature_profiles(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = 0,
        reference_count: Optional[bool] = False,
        **kw,
    ) -> Any:
        """
        Get all SD-ROUTING Feature Profiles with giving Family and profile type

        :param offset: Pagination offset
        :param limit: Pagination limit
        :param reference_count: get associated group details
        :returns: Any
        """
        params = {
            "offset": offset,
            "limit": limit,
            "referenceCount": reference_count,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/v1/feature-profile/sd-routing/sse", params=params, **kw
        )

    def create_sd_routing_sse_feature_profile(self, payload: Optional[str] = None, **kw) -> str:
        """
        Create a SD-ROUTING SSE Feature Profile

        :param payload: SD-ROUTING Feature profile
        :returns: str
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/sse",
            return_type=str,
            payload=payload,
            **kw,
        )

    def get_sd_routing_sse_feature_profile_by_profile_id(
        self, sse_id: str, references: Optional[bool] = False, **kw
    ) -> Any:
        """
        Get a SD-ROUTING SSE Feature Profile with sseId

        :param sse_id: Feature Profile Id
        :param references: get associated group details
        :returns: Any
        """
        params = {
            "sseId": sse_id,
            "references": references,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/v1/feature-profile/sd-routing/sse/{sseId}", params=params, **kw
        )

    def edit_sd_routing_sse_feature_profile(
        self, sse_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit a SD-ROUTING SSE Feature Profile

        :param sse_id: Feature Profile Id
        :param payload: SD-ROUTING Feature profile
        :returns: str
        """
        params = {
            "sseId": sse_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/sse/{sseId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sd_routing_sse_feature_profile(self, sse_id: str, **kw):
        """
        Delete Feature Profile

        :param sse_id: Sse id
        :returns: None
        """
        params = {
            "sseId": sse_id,
        }
        return self._request_adapter.request(
            "DELETE", "/dataservice/v1/feature-profile/sd-routing/sse/{sseId}", params=params, **kw
        )

    @property
    def cisco(self) -> CiscoBuilder:
        """
        The cisco property
        """
        from .cisco.cisco_builder import CiscoBuilder

        return CiscoBuilder(self._request_adapter)
