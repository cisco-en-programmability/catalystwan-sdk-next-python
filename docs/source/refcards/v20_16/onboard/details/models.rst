======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class DeviceDetails:
        """
        Device list to onboard
        """

        # host ip
        host: str
        # ssh password
        password: str
        # ssh username
        username: str
        # WAN interface name
        wan: str
        # device uuid/chassis number
        device_uuid: Optional[str]
        # enable password
        enable_password: Optional[str]
        # local file name
        local_file_name: Optional[str]
        # remote server file name
        remote_server_file_name: Optional[str]
        # remote server Id
        remote_server_id: Optional[str]


    class DeviceDetailsData:
        # Device list to onboard
        devices: List[DeviceDetails]


