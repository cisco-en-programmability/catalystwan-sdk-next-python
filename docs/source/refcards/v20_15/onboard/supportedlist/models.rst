======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class SupportedResponseUuid:
        device_mødel: Optional[str]
        is_autonomous_supported: Optional[bool]
        is_software_device: Optional[bool]
        is_system_ip_pool_needed: Optional[bool]


    class SupportedResponse:
        uuid: Optional[SupportedResponseUuid]


