======
Models
======


.. code:: python

    from typing import Literal, Optional, List, Union, Dict, Any

    Health = Literal["fair", "good", "poor"]


    class NetworkAvailabilityResp:
        health: Health
        jitter: int
        latency: int
        loss: int
        availability: Optional[int]
        latitude: Optional[str]
        longitude: Optional[str]
        siteid: Optional[str]
        sitename: Optional[str]


