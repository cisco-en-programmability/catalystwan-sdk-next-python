======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class GenerateDeactivateInfoData:
        available_versions: Optional[List[str]]
        device_model: Optional[str]
        device_type: Optional[str]
        host_name: Optional[str]
        personality: Optional[str]
        platform: Optional[str]
        reachability: Optional[str]
        site_id: Optional[str]
        system_ip: Optional[str]
        uptime_date: Optional[str]
        uuid: Optional[str]
        version: Optional[str]


    class GenerateDeactivateInfo:
        data: Optional[List[GenerateDeactivateInfoData]]


    class DeviceIp:
        """
        This is the valid DeviceIP
        """

        device_ip: Optional[str]


