======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class GenerateDeviceListData:
        available_versions: Optional[List[str]]
        current_partition: Optional[str]
        default_version: Optional[str]
        device_model: Optional[str]
        device_os: Optional[str]
        device_type: Optional[str]
        host_name: Optional[str]
        is_multi_step_upgrade_supported: Optional[bool]
        is_schedule_upgrade_supported: Optional[bool]
        layout_level: Optional[int]
        local_system_ip: Optional[str]
        personality: Optional[str]
        platform: Optional[str]
        platform_family: Optional[str]
        reachability: Optional[str]
        site_id: Optional[str]
        system_ip: Optional[str]
        uptime_date: Optional[int]
        uuid: Optional[str]
        version: Optional[str]


    class GenerateDeviceList:
        data: Optional[List[GenerateDeviceListData]]


