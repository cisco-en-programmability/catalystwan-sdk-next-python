======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class AdminTechCreateReq:
        custom_commands: Optional[List[str]]
        device_ip: Optional[str]
        device_type: Optional[str]
        exclude_cores: Optional[bool]
        exclude_logs: Optional[bool]
        exclude_tech: Optional[bool]
        tech_filter: Optional[List[str]]


