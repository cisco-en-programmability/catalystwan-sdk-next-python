======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class AppListDetails:
        created_by: Optional[str]
        id: Optional[str]
        name: Optional[str]
        type_: Optional[str]
        version: Optional[str]


    class PolicyComplianceApplications:
        new_applications: Optional[List[str]]
        old_applications: Optional[List[str]]


    class PolicyDetails:
        id: Optional[str]
        name: Optional[str]
        type_: Optional[str]
        version: Optional[str]


    class PolicyComplianceDetails:
        app_list: Optional[AppListDetails]
        applications: Optional[List[PolicyComplianceApplications]]
        policy: Optional[List[PolicyDetails]]


    class PolicyComplianceResponse:
        count: Optional[int]
        data: Optional[List[PolicyComplianceDetails]]


    class ApplicationRequestDetails:
        app_name: Optional[str]


    class ExtendedApplicationRequestData:
        data: Optional[List[ApplicationRequestDetails]]
        select_all: Optional[bool]


