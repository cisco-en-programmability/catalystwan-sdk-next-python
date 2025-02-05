# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .policy.policy_builder import PolicyBuilder
    from .unified.unified_builder import UnifiedBuilder


class EmbeddedSecurityBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/embedded-security
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sd_routing_embedded_security_feature_profiles(
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
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/embedded-security",
            params=params,
            **kw,
        )

    def create_sd_routing_embedded_security_feature_profile(
        self, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Create a SD-ROUTING Embedded Security Feature Profile

        :param payload: SD-ROUTING Feature profile
        :returns: str
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/embedded-security",
            return_type=str,
            payload=payload,
            **kw,
        )

    def get_sd_routing_embedded_security_feature_profile_by_profile_id(
        self,
        embedded_security_id: str,
        details: Optional[bool] = False,
        references: Optional[bool] = False,
        **kw,
    ) -> Any:
        """
        Get a SD-ROUTING Embedded Security Feature Profile with embeddedSecurityId

        :param embedded_security_id: Feature Profile Id
        :param details: get feature details
        :param references: get associated group details
        :returns: Any
        """
        params = {
            "embeddedSecurityId": embedded_security_id,
            "details": details,
            "references": references,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/embedded-security/{embeddedSecurityId}",
            params=params,
            **kw,
        )

    def edit_sd_routing_embedded_security_feature_profile(
        self, embedded_security_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit a SD-ROUTING Embedded Security Feature Profile

        :param embedded_security_id: Feature Profile Id
        :param payload: SD-ROUTING Feature profile
        :returns: str
        """
        params = {
            "embeddedSecurityId": embedded_security_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/embedded-security/{embeddedSecurityId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sd_routing_embedded_security_feature_profile(self, embedded_security_id: str, **kw):
        """
        Delete Feature Profile

        :param embedded_security_id: Embedded security id
        :returns: None
        """
        params = {
            "embeddedSecurityId": embedded_security_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/embedded-security/{embeddedSecurityId}",
            params=params,
            **kw,
        )

    @property
    def policy(self) -> PolicyBuilder:
        """
        The policy property
        """
        from .policy.policy_builder import PolicyBuilder

        return PolicyBuilder(self._request_adapter)

    @property
    def unified(self) -> UnifiedBuilder:
        """
        The unified property
        """
        from .unified.unified_builder import UnifiedBuilder

        return UnifiedBuilder(self._request_adapter)
