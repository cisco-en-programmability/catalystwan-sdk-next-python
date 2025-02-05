======
Models
======


.. code:: python

    from typing import Union, Dict, Optional, Literal, List, Any

    LastNHoursParam = Literal["1", "12", "24", "3", "6"]

    HealthParam = Literal["FAIR", "GOOD", "POOR"]


    class ApplicationsSitesItem:
        application: str
        fair_site: int
        family: str
        good_site: int
        health: str
        poor_site: int


