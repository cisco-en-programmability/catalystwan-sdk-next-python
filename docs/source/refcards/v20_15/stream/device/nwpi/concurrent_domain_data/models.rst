======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class ConcurrentDomainDataResponsePayloadInner:
        """
        Concurrent Domain Data schema for GET response
        """

        data: Optional[Any]
        flow_key: Optional[str]
        received_timestamp: Optional[int]
        trace_id: Optional[int]


