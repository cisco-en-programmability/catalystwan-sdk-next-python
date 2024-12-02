======
Models
======


.. code:: python

    from typing import Literal, Optional, List, Union, Dict, Any

    LastNHoursParam = Literal["1", "12", "24", "3", "6"]

    HealthParam = Literal["FAIR", "GOOD", "POOR"]


    class ApplicationsSiteItem:
        application: str
        family: str
        health: str
        jitter: int
        latency: int
        loss: int


