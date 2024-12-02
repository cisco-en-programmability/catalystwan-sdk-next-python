======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class GenerateRebootDeviceListData:
        available_services: Optional[List[str]]
        device_model: Optional[str]
        device_os: Optional[str]
        device_type: Optional[str]
        host_name: Optional[str]
        layout_level: Optional[int]
        local_system_ip: Optional[str]
        personality: Optional[str]
        platform: Optional[str]
        reachability: Optional[str]
        site_id: Optional[str]
        system_ip: Optional[str]
        uptime_date: Optional[int]
        uuid: Optional[str]
        version: Optional[str]


    class GenerateRebootDeviceList:
        data: Optional[List[GenerateRebootDeviceListData]]


