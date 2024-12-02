======
Models
======


.. code:: python

    from typing import Literal, Optional, List, Union, Dict, Any

    HealthParam = Literal["FAIR", "GOOD", "POOR"]


    class ApplicationSiteItem:
        health: str
        jitter: int
        latency: int
        loss: int
        path: str
        qoe: Optional[int]


