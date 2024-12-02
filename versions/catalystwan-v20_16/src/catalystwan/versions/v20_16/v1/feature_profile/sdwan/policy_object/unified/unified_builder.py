# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import SecurityProfileParcelTypeParam

if TYPE_CHECKING:
    from .advanced_inspection_profile.advanced_inspection_profile_builder import (
        AdvancedInspectionProfileBuilder,
    )
    from .advanced_malware_protection.advanced_malware_protection_builder import (
        AdvancedMalwareProtectionBuilder,
    )
    from .intrusion_prevention.intrusion_prevention_builder import IntrusionPreventionBuilder
    from .ssl_decryption.ssl_decryption_builder import SslDecryptionBuilder
    from .ssl_decryption_profile.ssl_decryption_profile_builder import SslDecryptionProfileBuilder
    from .url_filtering.url_filtering_builder import UrlFilteringBuilder


class UnifiedBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified
    """

    m = models

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
        Get Security Features for a given ParcelType

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

    def create_security_profile_parcel(
        self,
        policy_object_id: str,
        security_profile_parcel_type: SecurityProfileParcelTypeParam,
        payload: Optional[str] = None,
        **kw,
    ) -> str:
        """
        Create Feature for Security Policy

        :param policy_object_id: Feature Profile ID
        :param security_profile_parcel_type: Policy Object ListType
        :param payload: Security Feature
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

    def get_security_profile_parcel_by_parcel_id(
        self,
        policy_object_id: str,
        security_profile_parcel_type: SecurityProfileParcelTypeParam,
        security_profile_parcel_id: str,
        references: Optional[bool] = False,
        **kw,
    ) -> str:
        """
        Get Security Feature by FeatureId

        :param policy_object_id: Feature Profile ID
        :param security_profile_parcel_type: Policy Object ListType
        :param security_profile_parcel_id: Feature ID
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

    def edit_security_profile_parcel(
        self,
        policy_object_id: str,
        security_profile_parcel_type: SecurityProfileParcelTypeParam,
        security_profile_parcel_id: str,
        payload: Optional[str] = None,
        **kw,
    ) -> str:
        """
        Update a Security Feature

        :param policy_object_id: Feature Profile ID
        :param security_profile_parcel_type: Policy Object ListType
        :param security_profile_parcel_id: Feature ID
        :param payload: Security Feature
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

    def delete_security_profile_parcel(
        self,
        policy_object_id: str,
        security_profile_parcel_type: SecurityProfileParcelTypeParam,
        security_profile_parcel_id: str,
        **kw,
    ):
        """
        Delete a Security Feature

        :param policy_object_id: Feature Profile ID
        :param security_profile_parcel_type: Policy Object ListType
        :param security_profile_parcel_id: Feature ID
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

    @property
    def advanced_inspection_profile(self) -> AdvancedInspectionProfileBuilder:
        """
        The advanced-inspection-profile property
        """
        from .advanced_inspection_profile.advanced_inspection_profile_builder import (
            AdvancedInspectionProfileBuilder,
        )

        return AdvancedInspectionProfileBuilder(self._request_adapter)

    @property
    def advanced_malware_protection(self) -> AdvancedMalwareProtectionBuilder:
        """
        The advanced-malware-protection property
        """
        from .advanced_malware_protection.advanced_malware_protection_builder import (
            AdvancedMalwareProtectionBuilder,
        )

        return AdvancedMalwareProtectionBuilder(self._request_adapter)

    @property
    def intrusion_prevention(self) -> IntrusionPreventionBuilder:
        """
        The intrusion-prevention property
        """
        from .intrusion_prevention.intrusion_prevention_builder import IntrusionPreventionBuilder

        return IntrusionPreventionBuilder(self._request_adapter)

    @property
    def ssl_decryption(self) -> SslDecryptionBuilder:
        """
        The ssl-decryption property
        """
        from .ssl_decryption.ssl_decryption_builder import SslDecryptionBuilder

        return SslDecryptionBuilder(self._request_adapter)

    @property
    def ssl_decryption_profile(self) -> SslDecryptionProfileBuilder:
        """
        The ssl-decryption-profile property
        """
        from .ssl_decryption_profile.ssl_decryption_profile_builder import (
            SslDecryptionProfileBuilder,
        )

        return SslDecryptionProfileBuilder(self._request_adapter)

    @property
    def url_filtering(self) -> UrlFilteringBuilder:
        """
        The url-filtering property
        """
        from .url_filtering.url_filtering_builder import UrlFilteringBuilder

        return UrlFilteringBuilder(self._request_adapter)
