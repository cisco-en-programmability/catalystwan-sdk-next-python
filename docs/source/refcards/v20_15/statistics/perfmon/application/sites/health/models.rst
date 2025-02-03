======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    LastNHoursParam = Literal["1", "12", "24", "3", "6"]

    HealthParam = Literal["FAIR", "GOOD", "POOR"]


    class ApplicationSitesItem:
        fair_path: int
        good_path: int
        health: str
        poor_path: int
        siteid: str


