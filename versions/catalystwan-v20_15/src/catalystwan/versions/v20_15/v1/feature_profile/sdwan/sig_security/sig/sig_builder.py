# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface


class SigBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/sig-security/{sigSecurityId}/sig
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sig_security_profile_parcel_1(self, sig_security_id: str, **kw) -> str:
        """
        Get Sig Security Profile Parcels for a given ParcelType

        :param sig_security_id: Feature Profile ID
        :returns: str
        """
        params = {
            "sigSecurityId": sig_security_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/sig-security/{sigSecurityId}/sig",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_sig_security_profile_parcel_1(self):
        class create_sig_security_profile_parcel_1_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, sig_security_id: str, payload: Optional[str] = None, **kw) -> str:
                """
                Create Parcel for Sig Security Policy

                :param sig_security_id: Feature Profile ID
                :param payload: Sig Security Profile Parcel
                :returns: str
                """
                params = {
                    "sigSecurityId": sig_security_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/sig-security/{sigSecurityId}/sig",
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

        return create_sig_security_profile_parcel_1_(self._request_adapter)

    def get_sig_security_profile_parcel_by_parcel_id_1(
        self, sig_security_id: str, sig_security_profile_parcel_id: str, **kw
    ) -> str:
        """
        Get SigSecurity Profile Parcel by parcelId

        :param sig_security_id: Feature Profile ID
        :param sig_security_profile_parcel_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "sigSecurityId": sig_security_id,
            "sigSecurityProfileParcelId": sig_security_profile_parcel_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/sig-security/{sigSecurityId}/sig/{sigSecurityProfileParcelId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_sig_security_profile_parcel_1(self):
        class edit_sig_security_profile_parcel_1_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, sig_security_id: str, sig_security_profile_parcel_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Update a Sig Security Profile Parcel

                :param sig_security_id: Feature Profile ID
                :param sig_security_profile_parcel_id: Profile Parcel ID
                :param payload: Sig Security Profile Parcel
                :returns: str
                """
                params = {
                    "sigSecurityId": sig_security_id,
                    "sigSecurityProfileParcelId": sig_security_profile_parcel_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/sig-security/{sigSecurityId}/sig/{sigSecurityProfileParcelId}",
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

        return edit_sig_security_profile_parcel_1_(self._request_adapter)

    def delete_sig_security_profile_parcel_1(self, sig_security_id: str, sig_security_profile_parcel_id: str, **kw):
        """
        Delete a SigSecurity Profile Parcel

        :param sig_security_id: Feature Profile ID
        :param sig_security_profile_parcel_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "sigSecurityId": sig_security_id,
            "sigSecurityProfileParcelId": sig_security_profile_parcel_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/sig-security/{sigSecurityId}/sig/{sigSecurityProfileParcelId}",
            params=params,
            **kw,
        )
