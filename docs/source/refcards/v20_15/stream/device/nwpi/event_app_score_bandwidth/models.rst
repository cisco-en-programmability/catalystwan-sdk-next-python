======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class EventAppScoreBandwidthResponsePayloadInner:
        """
        Event Application Performance Score and Bandwidth schema for GET response
        """

        data: Optional[Any]
        entry_time: Optional[int]
        trace_id: Optional[int]
        type_: Optional[str]


