======
Models
======


.. code:: python

    from typing import Literal, Optional, List, Union, Dict, Any

    TunnelTypeParam = Literal["loopbackCgw", "loopbackTransit"]


    class InlineResponse2002:
        loopback_cgw_color: Optional[List[str]]
        loopback_tunnel_color: Optional[List[str]]


