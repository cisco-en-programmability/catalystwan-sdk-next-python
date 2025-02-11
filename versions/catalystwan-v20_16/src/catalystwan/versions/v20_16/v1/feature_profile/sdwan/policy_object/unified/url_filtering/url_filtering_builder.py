# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Union

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import (
    CreateSecurityProfileParcelPostRequest11,
    CreateSecurityProfileParcelPostRequest12,
    CreateSecurityProfileParcelPostRequest21,
    CreateSecurityProfileParcelPostRequest31,
    CreateSecurityProfileParcelPostRequest41,
    CreateSecurityProfileParcelPostRequest61,
    CreateSecurityProfileParcelPostResponse,
    GetSecurityProfileParcelGetResponse,
)


class UrlFilteringBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/url-filtering
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def create_security_profile_parcel(
        self,
        policy_object_id: str,
        payload: Optional[
            Union[
                Union[
                    CreateSecurityProfileParcelPostRequest11,
                    CreateSecurityProfileParcelPostRequest12,
                ],
                Union[
                    CreateSecurityProfileParcelPostRequest21,
                    CreateSecurityProfileParcelPostRequest12,
                ],
                Union[
                    CreateSecurityProfileParcelPostRequest31,
                    CreateSecurityProfileParcelPostRequest12,
                ],
                Union[
                    CreateSecurityProfileParcelPostRequest41,
                    CreateSecurityProfileParcelPostRequest12,
                ],
                Union[
                    CreateSecurityProfileParcelPostRequest31,
                    CreateSecurityProfileParcelPostRequest12,
                ],
                Union[
                    CreateSecurityProfileParcelPostRequest61,
                    CreateSecurityProfileParcelPostRequest12,
                ],
                Union[
                    CreateSecurityProfileParcelPostRequest31,
                    CreateSecurityProfileParcelPostRequest12,
                ],
            ]
        ] = None,
        **kw,
    ) -> CreateSecurityProfileParcelPostResponse:
        """
        Create Feature for Security Policy

        :param policy_object_id: Feature Profile ID
        :param payload: Security Feature
        :returns: CreateSecurityProfileParcelPostResponse
        """
        params = {
            "policyObjectId": policy_object_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/url-filtering",
            return_type=CreateSecurityProfileParcelPostResponse,
            params=params,
            payload=payload,
            **kw,
        )

    def get_security_profile_parcel(
        self, policy_object_id: str, parcel_id: str, reference_count: Optional[bool] = False, **kw
    ) -> GetSecurityProfileParcelGetResponse:
        """
        Get Security Features for a given ParcelType

        :param policy_object_id: Feature Profile ID
        :param reference_count: get reference count
        :param parcel_id: Parcel ID
        :returns: GetSecurityProfileParcelGetResponse
        """
        params = {
            "policyObjectId": policy_object_id,
            "referenceCount": reference_count,
            "parcelId": parcel_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/url-filtering/{parcelId}",
            return_type=GetSecurityProfileParcelGetResponse,
            params=params,
            **kw,
        )
