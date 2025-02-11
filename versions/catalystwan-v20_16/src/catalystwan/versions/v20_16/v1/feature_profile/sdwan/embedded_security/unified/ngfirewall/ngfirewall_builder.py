# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import (
    CreateNgfirewallProfileParcelPostRequest,
    CreateNgfirewallProfileParcelPostResponse,
)


class NgfirewallBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/embedded-security/{securityId}/unified/ngfirewall
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_ngfirewall_profile_parcel(self, security_id: str, **kw) -> str:
        """
        Get Ngfirewall Feature

        :param security_id: Feature Profile ID
        :returns: str
        """
        params = {
            "securityId": security_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/embedded-security/{securityId}/unified/ngfirewall",
            return_type=str,
            params=params,
            **kw,
        )

    def create_ngfirewall_profile_parcel(
        self,
        security_id: str,
        payload: Optional[CreateNgfirewallProfileParcelPostRequest] = None,
        **kw,
    ) -> CreateNgfirewallProfileParcelPostResponse:
        """
        Create Feature for Ngfirewall Policy

        :param security_id: Feature Profile ID
        :param payload: Ngfirewall Feature
        :returns: CreateNgfirewallProfileParcelPostResponse
        """
        params = {
            "securityId": security_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sdwan/embedded-security/{securityId}/unified/ngfirewall",
            return_type=CreateNgfirewallProfileParcelPostResponse,
            params=params,
            payload=payload,
            **kw,
        )

    def get_ngfirewall_profile_parcel_by_parcel_id(
        self, security_id: str, security_profile_parcel_id: str, **kw
    ) -> str:
        """
        Get Ngfirewall Feature by FeatureId

        :param security_id: Feature Profile ID
        :param security_profile_parcel_id: Feature ID
        :returns: str
        """
        params = {
            "securityId": security_id,
            "securityProfileParcelId": security_profile_parcel_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/embedded-security/{securityId}/unified/ngfirewall/{securityProfileParcelId}",
            return_type=str,
            params=params,
            **kw,
        )

    def edit_ngfirewall_profile_parcel(
        self, security_id: str, security_profile_parcel_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Update a Ngfirewall Feature

        :param security_id: Feature Profile ID
        :param security_profile_parcel_id: Feature ID
        :param payload: Ngfirewall Feature
        :returns: str
        """
        params = {
            "securityId": security_id,
            "securityProfileParcelId": security_profile_parcel_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sdwan/embedded-security/{securityId}/unified/ngfirewall/{securityProfileParcelId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_ngfirewall_profile_parcel(
        self, security_id: str, security_profile_parcel_id: str, **kw
    ):
        """
        Delete a Ngfirewall Feature

        :param security_id: Feature Profile ID
        :param security_profile_parcel_id: Feature ID
        :returns: None
        """
        params = {
            "securityId": security_id,
            "securityProfileParcelId": security_profile_parcel_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/embedded-security/{securityId}/unified/ngfirewall/{securityProfileParcelId}",
            params=params,
            **kw,
        )
