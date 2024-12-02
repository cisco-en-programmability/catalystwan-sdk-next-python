======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class TraceFinFlowTimeRangeResponsePayloadInner:
        """
        Fin Flow schema for GET response
        """

        data: Optional[Any]
        data_received_timestamp: Optional[int]
        entry_time: Optional[int]
        tenant: Optional[str]
        trace_id: Optional[int]
        type_: Optional[str]


