======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class RoutingDetailResponsePayloadInner:
        """
        Routing details info schema for GET response
        """

        data: Optional[Any]
        entry_time: Optional[int]
        flow_key: Optional[str]
        trace_id: Optional[int]


