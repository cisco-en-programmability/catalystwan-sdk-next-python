======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class RadiusServer:
        host: str
        port: int
        secret: str


    class Radius:
        retransmit: Optional[int]
        server: Optional[List[RadiusServer]]
        timeout: Optional[int]


