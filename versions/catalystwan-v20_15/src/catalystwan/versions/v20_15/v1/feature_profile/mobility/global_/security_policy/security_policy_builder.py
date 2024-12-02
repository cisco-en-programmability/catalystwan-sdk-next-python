# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import CreateSecurityPolicyProfileParcelForMobilityPostRequest


class SecurityPolicyBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/mobility/global/{profileId}/securityPolicy
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_security_policy_profile_parcel_list_for_mobility(
        self, profile_id: str, **kw
    ) -> str:
        """
        Get an Mobility SecurityPolicy Profile Parcel list for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :returns: str
        """
        params = {
            "profileId": profile_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/securityPolicy",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_security_policy_profile_parcel_for_mobility(self):
        class create_security_policy_profile_parcel_for_mobility_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                profile_id: str,
                payload: Optional[
                    CreateSecurityPolicyProfileParcelForMobilityPostRequest
                ] = None,
                **kw,
            ) -> str:
                """
                Create an SecurityPolicy Profile Parcel for Mobility Global Feature Profile

                :param profile_id: Feature Profile ID
                :param payload: SecurityPolicy Profile Parcel
                :returns: str
                """
                params = {
                    "profileId": profile_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/mobility/global/{profileId}/securityPolicy",
                    return_type=str,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(
                self, *args, **kwargs
            ) -> CreateSecurityPolicyProfileParcelForMobilityPostRequest:
                return CreateSecurityPolicyProfileParcelForMobilityPostRequest(
                    *args, **kwargs
                )

            @property
            def payload_model(
                self,
            ) -> Type[CreateSecurityPolicyProfileParcelForMobilityPostRequest]:
                return CreateSecurityPolicyProfileParcelForMobilityPostRequest

        return create_security_policy_profile_parcel_for_mobility_(
            self._request_adapter
        )

    def get_security_policy_profile_parcel_for_mobility(
        self, profile_id: str, security_policy_id: str, **kw
    ) -> str:
        """
        Get an Mobility SecurityPolicy Profile Parcel for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :param security_policy_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "profileId": profile_id,
            "securityPolicyId": security_policy_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/securityPolicy/{securityPolicyId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_security_policy_profile_parcel_for_mobility(self):
        class edit_security_policy_profile_parcel_for_mobility_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                profile_id: str,
                security_policy_id: str,
                payload: Optional[
                    CreateSecurityPolicyProfileParcelForMobilityPostRequest
                ] = None,
                **kw,
            ):
                """
                Edit an Security Policy Profile Parcel for Mobility Global Feature Profile

                :param profile_id: Feature Profile ID
                :param security_policy_id: Profile Parcel ID
                :param payload: Security Policy Profile Parcel
                :returns: None
                """
                params = {
                    "profileId": profile_id,
                    "securityPolicyId": security_policy_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/mobility/global/{profileId}/securityPolicy/{securityPolicyId}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(
                self, *args, **kwargs
            ) -> CreateSecurityPolicyProfileParcelForMobilityPostRequest:
                return CreateSecurityPolicyProfileParcelForMobilityPostRequest(
                    *args, **kwargs
                )

            @property
            def payload_model(
                self,
            ) -> Type[CreateSecurityPolicyProfileParcelForMobilityPostRequest]:
                return CreateSecurityPolicyProfileParcelForMobilityPostRequest

        return edit_security_policy_profile_parcel_for_mobility_(self._request_adapter)

    def delete_security_policy_profile_parcel_for_mobility(
        self, profile_id: str, security_policy_id: str, **kw
    ):
        """
        Delete a Security Policy Profile Parcel for Mobility Global Feature Profile

        :param profile_id: Feature Profile ID
        :param security_policy_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "profileId": profile_id,
            "securityPolicyId": security_policy_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/mobility/global/{profileId}/securityPolicy/{securityPolicyId}",
            params=params,
            **kw,
        )
