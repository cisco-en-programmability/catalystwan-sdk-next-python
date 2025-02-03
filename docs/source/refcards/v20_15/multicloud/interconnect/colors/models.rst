======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    TunnelTypeParam = Literal["loopbackCgw", "loopbackTransit"]


    class InlineResponse2002:
        loopback_cgw_color: Optional[List[str]]
        loopback_tunnel_color: Optional[List[str]]


