======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    Authentication = Literal["ASCII", "PAP"]


    class TacacsServer:
        address: Optional[str]
        auth_port: Optional[int]
        key: Optional[str]
        priority: Optional[int]
        secret_key: Optional[str]
        source_vpn: Optional[int]
        vpn: Optional[int]
        vpn_ip_subnet: Optional[str]


    class Tacacs:
        authentication: Optional[Authentication]
        server: Optional[List[TacacsServer]]
        timeout: Optional[int]


