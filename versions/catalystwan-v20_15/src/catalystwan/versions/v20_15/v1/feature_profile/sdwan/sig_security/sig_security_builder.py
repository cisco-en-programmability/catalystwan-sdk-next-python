# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .sig.sig_builder import SigBuilder


class SigSecurityBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/sig-security
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdwan_sig_security_feature_profiles(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = 0,
        reference_count: Optional[bool] = False,
        **kw,
    ) -> Any:
        """
        Get all SDWAN Feature Profiles with giving Family and profile type

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
            "GET", "/dataservice/v1/feature-profile/sdwan/sig-security", params=params, **kw
        )

    def create_sdwan_sig_security_feature_profile(self, payload: Optional[str] = None, **kw) -> str:
        """
        Create a SDWAN Sig Security Feature Profile

        :param payload: SDWAN Feature profile
        :returns: str
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sdwan/sig-security",
            return_type=str,
            payload=payload,
            **kw,
        )

    def get_sdwan_sig_security_feature_profile_by_profile_id(
        self, sig_security_id: str, references: Optional[bool] = False, **kw
    ) -> Any:
        """
        Get a SDWAN Sig Security Feature Profile with sigSecurityId

        :param sig_security_id: Feature Profile Id
        :param references: get associated group details
        :returns: Any
        """
        params = {
            "sigSecurityId": sig_security_id,
            "references": references,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/sig-security/{sigSecurityId}",
            params=params,
            **kw,
        )

    def edit_sdwan_sig_security_feature_profile(
        self, sig_security_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit a SDWAN Sig Security Feature Profile

        :param sig_security_id: Feature Profile Id
        :param payload: SDWAN Feature profile
        :returns: str
        """
        params = {
            "sigSecurityId": sig_security_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sdwan/sig-security/{sigSecurityId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sdwan_sig_security_feature_profile(self, sig_security_id: str, **kw):
        """
        Delete Feature Profile

        :param sig_security_id: Sig security id
        :returns: None
        """
        params = {
            "sigSecurityId": sig_security_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/sig-security/{sigSecurityId}",
            params=params,
            **kw,
        )

    @property
    def sig(self) -> SigBuilder:
        """
        The sig property
        """
        from .sig.sig_builder import SigBuilder

        return SigBuilder(self._request_adapter)
