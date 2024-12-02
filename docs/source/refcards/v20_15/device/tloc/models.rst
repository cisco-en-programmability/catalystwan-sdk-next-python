======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class DeviceTlocDataWithBfd:
        bfd_sessions_down: Optional[int]
        bfd_sessions_up: Optional[int]
        color: Optional[str]
        control_connections_down: Optional[str]
        control_connections_up: Optional[int]
        system_ip: Optional[str]


