======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class EventFlowFromAppHopResponsePayloadInner:
        """
        Trace Event Flow From Application And Hop schema for GET response
        """

        data: Optional[Any]
        entry_time: Optional[int]
        tenant: Optional[str]
        trace_id: Optional[int]
        type_: Optional[str]


