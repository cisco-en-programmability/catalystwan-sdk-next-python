======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    Health = Literal["fair", "good", "poor"]


    class NetworkAvailabilityResp:
        health: Health  # pytype: disable=annotation-type-mismatch
        jitter: int
        latency: int
        loss: int
        availability: Optional[int]
        latitude: Optional[str]
        longitude: Optional[str]
        siteid: Optional[str]
        sitename: Optional[str]


