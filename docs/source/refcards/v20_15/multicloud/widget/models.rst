======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class WidgetStatusStatusList:
        count: Optional[int]
        message: Optional[str]
        name: Optional[str]
        status: Optional[str]


    class AllOfcloudWidgetCgwDeviceStatus:
        count: Optional[int]
        name: Optional[str]
        status_list: Optional[List[WidgetStatusStatusList]]
        unreachable_count: Optional[int]


    class WidgetStatus:
        count: Optional[int]
        name: Optional[str]
        status_list: Optional[List[WidgetStatusStatusList]]


    class CloudWidget:
        cgw_device_site_ids: Optional[List[str]]
        cgw_device_status: Optional[AllOfcloudWidgetCgwDeviceStatus]
        cgw_sites_status: Optional[WidgetStatus]
        cgw_status: Optional[WidgetStatus]
        cloud_gateway_solution: Optional[str]
        cloud_type: Optional[str]
        num_accounts: Optional[int]
        num_tags: Optional[int]
        num_tunnels: Optional[int]
        num_vpcs: Optional[int]
        num_vpns: Optional[int]


