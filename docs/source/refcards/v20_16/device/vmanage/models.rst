======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class DeviceVmanageResponseData:
        ip_address: Optional[str]


    class DeviceResponseHeader:
        generated_on: Optional[int]


    class DeviceVmanageResponse:
        data: Optional[DeviceVmanageResponseData]
        header: Optional[DeviceResponseHeader]


