======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    HealthParam = Literal["FAIR", "GOOD", "POOR"]


    class ApplicationSiteItem:
        health: str
        jitter: int
        latency: int
        loss: int
        path: str
        qoe: Optional[int]


