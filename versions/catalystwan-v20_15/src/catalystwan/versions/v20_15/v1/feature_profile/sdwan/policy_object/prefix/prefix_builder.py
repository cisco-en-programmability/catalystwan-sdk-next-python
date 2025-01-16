# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import (
    CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse,
    Default,
    GetDataPrefixProfileParcelForPolicyObjectGetResponse,
)


class PrefixBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/policy-object/{policyObjectId}/prefix
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def create_data_prefix_profile_parcel_for_security_policy_object(self):
        class create_data_prefix_profile_parcel_for_security_policy_object_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, policy_object_id: str, payload: Optional[Default] = None, **kw
            ) -> CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse:
                """
                Create a Data Prefix Profile Parcel for Security Policy Object feature profile

                :param policy_object_id: Feature Profile ID
                :param payload: Data Prefix Profile Parcel
                :returns: CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse
                """
                params = {
                    "policyObjectId": policy_object_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/prefix",
                    return_type=CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Default:
                return Default(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Default]:
                return Default

        return create_data_prefix_profile_parcel_for_security_policy_object_(self._request_adapter)

    def get_data_prefix_profile_parcel_for_policy_object(
        self, policy_object_id: str, parcel_id: str, reference_count: Optional[bool] = False, **kw
    ) -> GetDataPrefixProfileParcelForPolicyObjectGetResponse:
        """
        Get Data Prefix Profile Parcels for Policy Object feature profile

        :param policy_object_id: Feature Profile ID
        :param reference_count: get reference count
        :param parcel_id: Parcel ID
        :returns: GetDataPrefixProfileParcelForPolicyObjectGetResponse
        """
        params = {
            "policyObjectId": policy_object_id,
            "referenceCount": reference_count,
            "parcelId": parcel_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/prefix/{parcelId}",
            return_type=GetDataPrefixProfileParcelForPolicyObjectGetResponse,
            params=params,
            **kw,
        )
