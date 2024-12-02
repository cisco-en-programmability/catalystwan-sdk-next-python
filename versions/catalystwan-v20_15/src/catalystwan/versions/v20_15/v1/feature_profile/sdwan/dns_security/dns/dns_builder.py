# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface


class DnsBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/dns-security/{dnsSecurityId}/dns
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sig_security_profile_parcel(self, dns_security_id: str, **kw) -> str:
        """
        Get Sig Security Profile Parcels for a given ParcelType

        :param dns_security_id: Feature Profile ID
        :returns: str
        """
        params = {
            "dnsSecurityId": dns_security_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/dns-security/{dnsSecurityId}/dns",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_sig_security_profile_parcel(self):
        class create_sig_security_profile_parcel_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, dns_security_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Create Parcel for Sig Security Policy

                :param dns_security_id: Feature Profile ID
                :param payload: Sig Security Profile Parcel
                :returns: str
                """
                params = {
                    "dnsSecurityId": dns_security_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/dns-security/{dnsSecurityId}/dns",
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

        return create_sig_security_profile_parcel_(self._request_adapter)

    def get_sig_security_profile_parcel_by_parcel_id(
        self, dns_security_id: str, dns_security_profile_parcel_id: str, **kw
    ) -> str:
        """
        Get SigSecurity Profile Parcel by parcelId

        :param dns_security_id: Feature Profile ID
        :param dns_security_profile_parcel_id: Profile Parcel ID
        :returns: str
        """
        params = {
            "dnsSecurityId": dns_security_id,
            "dnsSecurityProfileParcelId": dns_security_profile_parcel_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/dns-security/{dnsSecurityId}/dns/{dnsSecurityProfileParcelId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_sig_security_profile_parcel(self):
        class edit_sig_security_profile_parcel_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                dns_security_id: str,
                dns_security_profile_parcel_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Update a Sig Security Profile Parcel

                :param dns_security_id: Feature Profile ID
                :param dns_security_profile_parcel_id: Profile Parcel ID
                :param payload: Sig Security Profile Parcel
                :returns: str
                """
                params = {
                    "dnsSecurityId": dns_security_id,
                    "dnsSecurityProfileParcelId": dns_security_profile_parcel_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/dns-security/{dnsSecurityId}/dns/{dnsSecurityProfileParcelId}",
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

        return edit_sig_security_profile_parcel_(self._request_adapter)

    def delete_sig_security_profile_parcel(
        self, dns_security_id: str, dns_security_profile_parcel_id: str, **kw
    ):
        """
        Delete a SigSecurity Profile Parcel

        :param dns_security_id: Feature Profile ID
        :param dns_security_profile_parcel_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "dnsSecurityId": dns_security_id,
            "dnsSecurityProfileParcelId": dns_security_profile_parcel_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/dns-security/{dnsSecurityId}/dns/{dnsSecurityProfileParcelId}",
            params=params,
            **kw,
        )
