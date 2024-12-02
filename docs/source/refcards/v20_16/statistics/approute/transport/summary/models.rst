======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class AppRouteFecAggRespInner:
        count: Optional[int]
        entry_time: Optional[str]
        fec_loss_recovery: Optional[str]
        loss_percentage: Optional[int]
        name: Optional[str]
        proto: Optional[str]
        state: Optional[str]


