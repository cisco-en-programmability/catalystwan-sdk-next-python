======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    HealthParam = Literal["FAIR", "GOOD", "POOR"]


    class ApplicationSiteItem:
        health: str
        jitter: int
        latency: int
        loss: int
        path: str
        qoe: Optional[int]


