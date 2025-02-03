======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    LastNHoursParam = Literal["1", "12", "24", "3", "6"]

    HealthParam = Literal["FAIR", "GOOD", "POOR"]


    class ApplicationsSitesItem:
        application: str
        fair_site: int
        family: str
        good_site: int
        health: str
        poor_site: int


