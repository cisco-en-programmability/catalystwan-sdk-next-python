======
Models
======


.. code:: python

    from typing import Union, Dict, Optional, Literal, List, Any

    LastNHoursParam = Literal["1", "12", "24", "3", "6"]

    HealthParam = Literal["FAIR", "GOOD", "POOR"]


    class ApplicationSitesItem:
        fair_path: int
        good_path: int
        health: str
        poor_path: int
        siteid: str


