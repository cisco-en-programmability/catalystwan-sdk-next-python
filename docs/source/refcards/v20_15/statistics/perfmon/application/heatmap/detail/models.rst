======
Models
======


.. code:: python

    from typing import List, Dict, Union, Literal, Optional, Any

    LastNHoursParam = Literal["1", "12", "24", "3", "6"]


    class ApplicationHeatMapDetail:
        fair_site: int
        good_site: int
        poor_site: int


