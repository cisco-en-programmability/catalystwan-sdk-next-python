======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class PowerConsumptionDeviceEntry:
        change: Optional[int]
        cost: Optional[int]
        device_model: Optional[str]
        device_type: Optional[str]
        emission: Optional[int]
        local_system_ip: Optional[str]
        name: Optional[str]
        power_usage: Optional[int]
        site_id: Optional[str]
        site_name: Optional[str]
        system_ip: Optional[str]
        uuid: Optional[str]


    class PowerConsumptionSiteEntry:
        change: Optional[int]
        cost: Optional[int]
        devices: Optional[List[PowerConsumptionDeviceEntry]]
        emission: Optional[int]
        power_usage: Optional[int]
        site_id: Optional[str]
        site_name: Optional[str]


    class PowerConsumptionDeviceResp:
        data: Optional[List[PowerConsumptionSiteEntry]]


