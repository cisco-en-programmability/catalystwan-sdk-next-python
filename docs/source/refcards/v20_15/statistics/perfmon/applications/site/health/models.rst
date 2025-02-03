======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    LastNHoursParam = Literal["1", "12", "24", "3", "6"]

    HealthParam = Literal["FAIR", "GOOD", "POOR"]


    class ApplicationsSiteItem:
        application: str
        family: str
        health: str
        jitter: int
        latency: int
        loss: int


