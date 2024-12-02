======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class QoSAggResp:
        count: Optional[int]
        entry_time: Optional[str]
        jitter: Optional[int]
        latency: Optional[int]
        local_color: Optional[str]
        loss_percentage: Optional[int]


