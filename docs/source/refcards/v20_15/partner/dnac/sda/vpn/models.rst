======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class Vpn:
        vpn_id: Optional[str]
        vpn_type: Optional[str]


    class VpnListResHeader:
        generated_on: Optional[int]


    class VpnListRes:
        data: Optional[List[Vpn]]
        header: Optional[VpnListResHeader]


