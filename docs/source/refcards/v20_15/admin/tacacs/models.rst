======
Models
======


.. code:: python

    from typing import Literal, Optional, List, Union, Dict, Any

    Authentication = Literal["ASCII", "PAP"]


    class TacacsServer:
        address: Optional[str]
        auth_port: Optional[int]
        key: Optional[str]
        priority: Optional[int]
        secret_key: Optional[str]
        vpn: Optional[int]
        vpn_ip_subnet: Optional[str]


    class Tacacs:
        authentication: Optional[Authentication]
        server: Optional[List[TacacsServer]]
        timeout: Optional[int]


