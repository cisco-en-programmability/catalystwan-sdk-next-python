======
Models
======


.. code:: python

    from typing import Union, Dict, Optional, Literal, List, Any

    HealthParam = Literal["FAIR", "GOOD", "POOR"]


    class ApplicationSiteItem:
        health: str
        jitter: int
        latency: int
        loss: int
        path: str
        qoe: Optional[int]


