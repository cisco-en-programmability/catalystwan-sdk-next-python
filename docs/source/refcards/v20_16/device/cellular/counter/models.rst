======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    TypeParam = Literal["carrier", "product", "rat"]

    LastNHoursParam = Literal["1", "12", "24", "3", "6"]


    class CellularCount:
        active: Optional[int]
        carrier: Optional[str]
        product: Optional[str]
        rat: Optional[str]
        standby: Optional[int]


