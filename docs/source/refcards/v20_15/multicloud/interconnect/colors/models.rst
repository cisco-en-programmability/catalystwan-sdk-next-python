======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    TunnelTypeParam = Literal["loopbackCgw", "loopbackTransit"]


    class InlineResponse2002:
        loopback_cgw_color: Optional[List[str]]
        loopback_tunnel_color: Optional[List[str]]


