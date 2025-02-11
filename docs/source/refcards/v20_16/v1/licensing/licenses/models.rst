======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class LicensesResponseLicenses:
        available: Optional[int]
        display_name: Optional[str]
        in_use: Optional[int]
        is_preferred: Optional[bool]
        tag: Optional[str]


    class LicensesResponseBaseLicenses:
        licenses: Optional[List[LicensesResponseLicenses]]
        platform_class: Optional[str]
        # List of device UUIDs
        uuids: Optional[List[str]]


    class LicensesResponseTenantLicenses:
        licenses: Optional[List[LicensesResponseLicenses]]
        total_tenant_lic_required: Optional[int]


    class LicensesResponse:
        base_licenses: Optional[List[LicensesResponseBaseLicenses]]
        tenant_licenses: Optional[LicensesResponseTenantLicenses]


    class AppliedFilters:
        billing_type: Optional[str]
        license_classification: Optional[str]


    class LicensesRequest:
        applied_filters: Optional[AppliedFilters]
        # List of device UUIDs
        uuids: Optional[List[str]]


