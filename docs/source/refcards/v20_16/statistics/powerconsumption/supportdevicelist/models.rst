======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class DeviceListEntry:
        device_model: Optional[str]
        local_system_ip: Optional[str]
        name: Optional[str]
        site_id: Optional[str]
        site_name: Optional[str]
        system_ip: Optional[str]
        uuid: Optional[str]


    class SupportedDeviceListEntry:
        device_model: Optional[str]
        has_estimated: Optional[bool]
        local_system_ip: Optional[str]
        name: Optional[str]
        site_id: Optional[str]
        site_name: Optional[str]
        system_ip: Optional[str]
        uuid: Optional[str]


    class SupportedDeviceList:
        devices: Optional[List[DeviceListEntry]]
        supported_devices: Optional[List[SupportedDeviceListEntry]]


