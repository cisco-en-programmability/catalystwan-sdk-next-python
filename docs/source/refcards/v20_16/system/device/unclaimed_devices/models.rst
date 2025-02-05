======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class GetAllUnclaimedDevices:
        _rid: Optional[int]
        chassis_number: Optional[str]
        create_time_stamp: Optional[int]
        lastupdated: Optional[int]
        org: Optional[str]
        serial_number: Optional[str]
        status: Optional[str]
        subject_serial_number: Optional[str]
        vdevice_data_key: Optional[str]
        vdevice_host_name: Optional[str]
        vdevice_name: Optional[str]
        vmanage_system_ip: Optional[str]


