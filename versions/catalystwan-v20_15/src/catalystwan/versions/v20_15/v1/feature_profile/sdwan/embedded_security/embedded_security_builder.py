# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import (
    CreateSdwanEmbeddedSecurityFeatureProfilePostRequest,
    CreateSdwanEmbeddedSecurityFeatureProfilePostResponse,
    GetSdwanEmbeddedSecurityFeatureProfilesGetResponse,
    GetSingleSdwanEmbeddedSecurityPayload,
)

if TYPE_CHECKING:
    from .policy.policy_builder import PolicyBuilder
    from .unified.unified_builder import UnifiedBuilder


class EmbeddedSecurityBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/embedded-security
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdwan_embedded_security_feature_profiles(
        self, offset: Optional[int] = None, limit: Optional[int] = 0, **kw
    ) -> List[GetSdwanEmbeddedSecurityFeatureProfilesGetResponse]:
        """
        Get all SDWAN Feature Profiles with giving Family and profile type

        :param offset: Pagination offset
        :param limit: Pagination limit
        :returns: List[GetSdwanEmbeddedSecurityFeatureProfilesGetResponse]
        """
        params = {
            "offset": offset,
            "limit": limit,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/embedded-security",
            return_type=List[GetSdwanEmbeddedSecurityFeatureProfilesGetResponse],
            params=params,
            **kw,
        )

    def create_sdwan_embedded_security_feature_profile(
        self, payload: Optional[CreateSdwanEmbeddedSecurityFeatureProfilePostRequest] = None, **kw
    ) -> CreateSdwanEmbeddedSecurityFeatureProfilePostResponse:
        """
        Create a SDWAN Embedded Security Feature Profile

        :param payload: SDWAN Feature profile
        :returns: CreateSdwanEmbeddedSecurityFeatureProfilePostResponse
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sdwan/embedded-security",
            return_type=CreateSdwanEmbeddedSecurityFeatureProfilePostResponse,
            payload=payload,
            **kw,
        )

    def get_sdwan_embedded_security_feature_profile_by_profile_id(
        self, embedded_security_id: str, details: Optional[bool] = False, **kw
    ) -> GetSingleSdwanEmbeddedSecurityPayload:
        """
        Get a SDWAN Embedded Security Feature Profile with embeddedSecurityId

        :param embedded_security_id: Feature Profile Id
        :param details: get feature details
        :returns: GetSingleSdwanEmbeddedSecurityPayload
        """
        params = {
            "embeddedSecurityId": embedded_security_id,
            "details": details,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/embedded-security/{embeddedSecurityId}",
            return_type=GetSingleSdwanEmbeddedSecurityPayload,
            params=params,
            **kw,
        )

    def edit_sdwan_embedded_security_feature_profile(
        self,
        embedded_security_id: str,
        payload: Optional[CreateSdwanEmbeddedSecurityFeatureProfilePostRequest] = None,
        **kw,
    ) -> CreateSdwanEmbeddedSecurityFeatureProfilePostResponse:
        """
        Edit a SDWAN Embedded Security Feature Profile

        :param embedded_security_id: Feature Profile Id
        :param payload: SDWAN Feature profile
        :returns: CreateSdwanEmbeddedSecurityFeatureProfilePostResponse
        """
        params = {
            "embeddedSecurityId": embedded_security_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sdwan/embedded-security/{embeddedSecurityId}",
            return_type=CreateSdwanEmbeddedSecurityFeatureProfilePostResponse,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sdwan_embedded_security_feature_profile(self, embedded_security_id: str, **kw):
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
            "/dataservice/v1/feature-profile/sdwan/embedded-security/{embeddedSecurityId}",
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
