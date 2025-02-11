======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class RealTimeData:
        component_cname: Optional[str]
        lastupdated: Optional[int]
        platform_property_configurable: Optional[str]
        platform_property_name: Optional[str]
        value_string: Optional[str]
        vdevice_data_key: Optional[str]
        vdevice_host_name: Optional[str]
        vdevice_name: Optional[str]


    class PowerConsumptionRealTime:
        data: Optional[List[RealTimeData]]


    class DeviceIp:
        """
        This is the valid DeviceIP
        """

        device_ip: Optional[str]


