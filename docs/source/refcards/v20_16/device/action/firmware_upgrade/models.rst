======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class FirmwareImageRemoteUpgradeDevices:
        device_id: Optional[str]
        device_ip: Optional[str]


    class FirmwareImageRemoteUpgradeInputData:
        family: Optional[str]
        remote_server_id: Optional[str]
        version: Optional[str]


    class FirmwareImageRemoteUpgradeInput:
        data: Optional[List[FirmwareImageRemoteUpgradeInputData]]
        version_type: Optional[str]


    class FirmwareImageRemoteUpgrade:
        action: Optional[str]
        action_end: Optional[str]
        action_end_millis: Optional[int]
        action_name: Optional[str]
        action_start: Optional[str]
        action_start_millis: Optional[int]
        device_type: Optional[str]
        devices: Optional[List[FirmwareImageRemoteUpgradeDevices]]
        input: Optional[FirmwareImageRemoteUpgradeInput]
        time_zone: Optional[str]


