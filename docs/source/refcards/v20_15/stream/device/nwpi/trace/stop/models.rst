======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class NwpiTraceStopRespPayloadTraces:
        action: Optional[str]
        device_ip: Optional[str]
        entry_time: Optional[int]
        local_system_ip: Optional[str]
        message: Optional[str]
        trace_id: Optional[int]
        uuid: Optional[str]


    class NwpiTraceStopRespPayload:
        """
        Nwpi trace stoppayload schema
        """

        action: Optional[str]
        domain_mon: Optional[bool]
        entry_time: Optional[int]
        message: Optional[str]
        qos_mon: Optional[bool]
        state: Optional[str]
        trace_id: Optional[str]
        trace_name: Optional[str]
        traces: Optional[List[NwpiTraceStopRespPayloadTraces]]


