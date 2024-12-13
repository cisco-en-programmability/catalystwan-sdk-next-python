======
Models
======


.. code:: python

    from typing import List, Dict, Union, Literal, Optional, Any

    HealthParam = Literal["FAIR", "GOOD", "POOR"]


    class ApplicationSiteItem:
        health: str
        jitter: int
        latency: int
        loss: int
        path: str
        qoe: Optional[int]


