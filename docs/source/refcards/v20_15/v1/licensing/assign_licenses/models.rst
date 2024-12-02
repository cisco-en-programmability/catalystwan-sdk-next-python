======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class AssignLicensesRequestAssignLicenses:
        allocated: Optional[int]
        billing_type: Optional[str]
        display_name: Optional[str]
        sa_name: Optional[str]
        subscription_id: Optional[str]
        tag: Optional[str]
        va_name: Optional[str]


    class AssignLicensesRequestBaseLicenses:
        assign_licenses: Optional[
            List[AssignLicensesRequestAssignLicenses]
        ]
        # List of device UUIDs
        uuids: Optional[List[str]]


    class AssignLicensesRequest:
        base_licenses: Optional[List[AssignLicensesRequestBaseLicenses]]
        tenant_licenses: Optional[
            List[AssignLicensesRequestAssignLicenses]
        ]


