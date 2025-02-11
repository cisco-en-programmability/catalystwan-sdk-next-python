======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class SaVaDistributionResponseSaVaMap:
        allocated: Optional[int]
        available: Optional[int]
        in_use: Optional[int]
        sa_name: Optional[str]
        subscription_id: Optional[str]
        va_name: Optional[str]


    class SaVaDistributionResponseBaseLicenses:
        display_name: Optional[str]
        platform_class: Optional[str]
        sava_map: Optional[List[SaVaDistributionResponseSaVaMap]]
        tag: Optional[str]
        # List of device UUIDs
        uuids: Optional[List[str]]


    class SaVaDistributionResponseTenantLicenses:
        display_name: Optional[str]
        sava_map: Optional[List[SaVaDistributionResponseSaVaMap]]
        tag: Optional[str]


    class SaVaDistributionResponse:
        base_licenses: Optional[
            List[SaVaDistributionResponseBaseLicenses]
        ]
        tenant_licenses: Optional[SaVaDistributionResponseTenantLicenses]


    class AppliedFilters:
        billing_type: Optional[str]
        license_classification: Optional[str]


    class SaVaDistributionRequestBaseLicenses:
        display_name: Optional[str]
        platform_class: Optional[str]
        tag: Optional[str]
        # List of device UUIDs
        uuids: Optional[List[str]]


    class SaVaDistributionRequestTenantLicense:
        display_name: Optional[str]
        tag: Optional[str]
        total_tenant_lic_required: Optional[int]


    class SaVaDistributionRequest:
        applied_filters: Optional[AppliedFilters]
        base_licenses: Optional[List[SaVaDistributionRequestBaseLicenses]]
        tenant_licenses: Optional[SaVaDistributionRequestTenantLicense]


