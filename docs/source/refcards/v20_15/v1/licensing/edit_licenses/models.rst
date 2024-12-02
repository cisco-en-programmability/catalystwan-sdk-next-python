======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class AppliedFilters:
        billing_type: Optional[str]
        license_classification: Optional[str]


    class EditLicenseResponseLicenses:
        available: Optional[int]
        display_name: Optional[str]
        in_use: Optional[int]
        is_assigned: Optional[bool]
        tag: Optional[str]


    class EditLicenseResponseBaseLicenses:
        licenses: Optional[List[EditLicenseResponseLicenses]]
        platform_class: Optional[str]


    class EditLicenseResponseTenantLicenses:
        licenses: Optional[List[EditLicenseResponseLicenses]]
        total_tenant_lic_required: Optional[int]


    class EditLicenseResponse:
        applied_filters: Optional[AppliedFilters]
        base_licenses: Optional[EditLicenseResponseBaseLicenses]
        tenant_licenses: Optional[EditLicenseResponseTenantLicenses]


