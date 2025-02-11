======
Models
======


.. code:: python

    from typing import Union, Dict, Optional, Literal, List, Any

    TypeParam = Literal["carrier", "rat"]

    LastNHoursParam = Literal["1", "12", "24", "3", "6"]


    class CellularHealth:
        carrier: Optional[str]
        excellent: Optional[int]
        fair: Optional[int]
        good: Optional[int]
        poor: Optional[int]
        rat: Optional[str]


