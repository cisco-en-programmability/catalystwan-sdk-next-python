======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class GenerateRediscoverInfoData:
        board_serial: Optional[str]
        certificate_validity: Optional[str]
        connected_v_manages: Optional[List[str]]
        control_connections: Optional[str]
        device_groups: Optional[List[str]]
        device_id: Optional[str]
        device_model: Optional[str]
        device_os: Optional[str]
        device_type: Optional[str]
        domain_id: Optional[str]
        host_name: Optional[str]
        is_device_geo_data: Optional[bool]
        lastupdated: Optional[int]
        latitude: Optional[str]
        layout_level: Optional[int]
        local_system_ip: Optional[str]
        longitude: Optional[str]
        max_controllers: Optional[str]
        model_sku: Optional[str]
        personality: Optional[str]
        platform: Optional[str]
        reachability: Optional[str]
        site_id: Optional[str]
        state: Optional[str]
        state_description: Optional[str]
        status: Optional[str]
        status_order: Optional[int]
        system_ip: Optional[str]
        testbed_mode: Optional[bool]
        timezone: Optional[str]
        total_cpu_count: Optional[str]
        uptime_date: Optional[int]
        uuid: Optional[str]
        validity: Optional[str]
        version: Optional[str]


    class GenerateRediscoverInfo:
        data: Optional[List[GenerateRediscoverInfoData]]


