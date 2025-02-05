======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class SdaDeviceConfigRes:
        id: Optional[str]


    class DeviceConfig:
        device_config: Optional[str]
        device_id: Optional[str]


    class VpnListResHeader:
        generated_on: Optional[int]


    class SdaConfigRequest:
        data: Optional[List[DeviceConfig]]
        header: Optional[VpnListResHeader]


