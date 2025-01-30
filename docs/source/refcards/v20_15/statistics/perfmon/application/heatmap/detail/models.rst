======
Models
======


.. code:: python

    from typing import Literal, Any, Union, Dict, Optional, List

    LastNHoursParam = Literal["1", "12", "24", "3", "6"]


    class ApplicationHeatMapDetail:
        fair_site: int
        good_site: int
        poor_site: int


