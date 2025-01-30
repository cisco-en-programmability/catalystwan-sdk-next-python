======
Models
======


.. code:: python

    from typing import List, Dict, Optional, Union, Any, Literal

    HealthParam = Literal["FAIR", "GOOD", "POOR"]


    class ApplicationSiteItem:
        health: str
        jitter: int
        latency: int
        loss: int
        path: str
        qoe: Optional[int]


