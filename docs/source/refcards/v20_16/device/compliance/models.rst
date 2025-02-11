======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    OrderByParam = Literal["asc", "desc"]


    class DeviceCheckList:
        message: Optional[str]
        status: Optional[str]
        type_: Optional[str]


    class DeviceApiDetails:
        chassis_number: Optional[str]
        current_version: Optional[str]
        device_type: Optional[str]
        host_name: Optional[str]
        local_system_ip: Optional[str]
        personality: Optional[str]
        reachability: Optional[str]
        site_id: Optional[str]
        site_name: Optional[str]
        system_ip: Optional[str]
        uuid: Optional[str]


    class DeviceComplianceApiData:
        check_list: Optional[List[DeviceCheckList]]
        device_details: Optional[DeviceApiDetails]
        status: Optional[str]


    class DeviceComplianceApiResponse:
        count: Optional[int]
        devices: Optional[List[DeviceComplianceApiData]]


