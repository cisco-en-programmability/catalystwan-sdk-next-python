# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface


class PolicyBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/embedded-security/{securityId}/policy
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_security_profile_parcel_1(self, security_id: str, **kw) -> str:
        """
        Get Security Profile Parcels for a given ParcelType

        :param security_id: Feature Profile ID
        :returns: str
        """
        params = {
            "securityId": security_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/embedded-security/{securityId}/policy",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_embedded_security_profile_parcel(self):
        class create_embedded_security_profile_parcel_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, security_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Create Parcel for Security Policy

                :param security_id: Feature Profile ID
                :param payload: Security Profile Parcel
                :returns: str
                """
                params = {
                    "securityId": security_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/embedded-security/{securityId}/policy",
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

        return create_embedded_security_profile_parcel_(self._request_adapter)

    def get_security_profile_parcel_by_parcel_id_1(
        self, security_id: str, security_profile_parcel_id: str, **kw
    ) -> str:
        """
        Get Security Profile Parcel by parcelId

        :param security_id: Feature Profile ID
        :param security_profile_parcel_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "securityId": security_id,
            "securityProfileParcelId": security_profile_parcel_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/embedded-security/{securityId}/policy/{securityProfileParcelId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_security_profile_parcel_1(self):
        class edit_security_profile_parcel_1_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                security_id: str,
                security_profile_parcel_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Update a Security Profile Parcel

                :param security_id: Feature Profile ID
                :param security_profile_parcel_id: Profile Parcel ID
                :param payload: Security Profile Parcel
                :returns: str
                """
                params = {
                    "securityId": security_id,
                    "securityProfileParcelId": security_profile_parcel_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/embedded-security/{securityId}/policy/{securityProfileParcelId}",
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

        return edit_security_profile_parcel_1_(self._request_adapter)

    def delete_security_profile_parcel_1(
        self, security_id: str, security_profile_parcel_id: str, **kw
    ):
        """
        Delete a Security Profile Parcel

        :param security_id: Feature Profile ID
        :param security_profile_parcel_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "securityId": security_id,
            "securityProfileParcelId": security_profile_parcel_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/embedded-security/{securityId}/policy/{securityProfileParcelId}",
            params=params,
            **kw,
        )
