======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class DeviceCountersData:
        crash_count: Optional[int]
        expected_control_connections: Optional[int]
        number_vsmart_control_connections: Optional[int]
        reboot_count: Optional[int]
        system_ip: Optional[str]


    class DeviceResponseHeader:
        generated_on: Optional[int]


    class DeviceCountersResponse:
        data: Optional[List[DeviceCountersData]]
        header: Optional[DeviceResponseHeader]


