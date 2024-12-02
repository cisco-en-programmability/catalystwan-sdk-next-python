# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface
from .models import SecurityProfileParcelTypeParam


class UnifiedBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_security_profile_parcel(
        self,
        policy_object_id: str,
        security_profile_parcel_type: SecurityProfileParcelTypeParam,
        reference_count: Optional[bool] = False,
        **kw,
    ) -> str:
        """
        Get Security Profile Parcels for a given ParcelType

        :param policy_object_id: Feature Profile ID
        :param security_profile_parcel_type: Policy Object ListType
        :param reference_count: get reference count
        :returns: str
        """
        params = {
            "policyObjectId": policy_object_id,
            "securityProfileParcelType": security_profile_parcel_type,
            "referenceCount": reference_count,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/{securityProfileParcelType}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_security_profile_parcel(self):
        class create_security_profile_parcel_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                policy_object_id: str,
                security_profile_parcel_type: SecurityProfileParcelTypeParam,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Create Parcel for Security Policy

                :param policy_object_id: Feature Profile ID
                :param security_profile_parcel_type: Policy Object ListType
                :param payload: Security Profile Parcel
                :returns: str
                """
                params = {
                    "policyObjectId": policy_object_id,
                    "securityProfileParcelType": security_profile_parcel_type,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/{securityProfileParcelType}",
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

        return create_security_profile_parcel_(self._request_adapter)

    def get_security_profile_parcel_by_parcel_id(
        self,
        policy_object_id: str,
        security_profile_parcel_type: SecurityProfileParcelTypeParam,
        security_profile_parcel_id: str,
        references: Optional[bool] = False,
        **kw,
    ) -> str:
        """
        Get Security Profile Parcel by parcelId

        :param policy_object_id: Feature Profile ID
        :param security_profile_parcel_type: Policy Object ListType
        :param security_profile_parcel_id: Profile Parcel ID
        :param references: get associated profile/parcel details
        :returns: str
        """
        params = {
            "policyObjectId": policy_object_id,
            "securityProfileParcelType": security_profile_parcel_type,
            "securityProfileParcelId": security_profile_parcel_id,
            "references": references,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/{securityProfileParcelType}/{securityProfileParcelId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_security_profile_parcel(self):
        class edit_security_profile_parcel_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                policy_object_id: str,
                security_profile_parcel_type: SecurityProfileParcelTypeParam,
                security_profile_parcel_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Update a Security Profile Parcel

                :param policy_object_id: Feature Profile ID
                :param security_profile_parcel_type: Policy Object ListType
                :param security_profile_parcel_id: Profile Parcel ID
                :param payload: Security Profile Parcel
                :returns: str
                """
                params = {
                    "policyObjectId": policy_object_id,
                    "securityProfileParcelType": security_profile_parcel_type,
                    "securityProfileParcelId": security_profile_parcel_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/{securityProfileParcelType}/{securityProfileParcelId}",
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

        return edit_security_profile_parcel_(self._request_adapter)

    def delete_security_profile_parcel(
        self,
        policy_object_id: str,
        security_profile_parcel_type: SecurityProfileParcelTypeParam,
        security_profile_parcel_id: str,
        **kw,
    ):
        """
        Delete a Security Profile Parcel

        :param policy_object_id: Feature Profile ID
        :param security_profile_parcel_type: Policy Object ListType
        :param security_profile_parcel_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "policyObjectId": policy_object_id,
            "securityProfileParcelType": security_profile_parcel_type,
            "securityProfileParcelId": security_profile_parcel_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/{securityProfileParcelType}/{securityProfileParcelId}",
            params=params,
            **kw,
        )
