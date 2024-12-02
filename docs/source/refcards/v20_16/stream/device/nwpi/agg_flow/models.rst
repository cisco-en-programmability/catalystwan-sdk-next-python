======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class AggFlowResponsePayloadInner:
        """
        Aggregated flow data  schema for GET response
        """

        data: Optional[Any]
        entry_time: Optional[int]
        tenant: Optional[str]
        trace_id: Optional[int]
        type_: Optional[str]


