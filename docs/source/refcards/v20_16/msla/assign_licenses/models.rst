======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class AssignMslaLicensesBaseLicense:
        billing_type: Optional[str]
        license_type: Optional[str]
        sa_id: Optional[str]
        subscription_id: Optional[str]
        tag: Optional[str]
        va_id: Optional[str]


    class AssignMslaLicensesTenantLicense:
        billing_type: Optional[str]
        count: Optional[int]
        license_type: Optional[str]
        sa_id: Optional[str]
        subscription_id: Optional[str]
        tag: Optional[str]
        va_id: Optional[str]


    class AssignMslaLicenses:
        base_license: Optional[AssignMslaLicensesBaseLicense]
        tenant_license: Optional[List[AssignMslaLicensesTenantLicense]]
        uuid: Optional[List[str]]


