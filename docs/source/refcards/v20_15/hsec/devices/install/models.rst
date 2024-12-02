======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class GetHsecDevicesPayloadInner:
        configured_system_ip: Optional[str]
        device_model: Optional[str]
        host_name: Optional[str]
        hsec_license_status: Optional[str]
        is_hsec_supported: Optional[bool]
        reachability: Optional[str]
        tag: Optional[str]
        uuid: Optional[str]


