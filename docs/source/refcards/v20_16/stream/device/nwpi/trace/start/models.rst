======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class NwpiTraceStartRespPayloadTraces:
        device_ip: Optional[str]
        entry_time: Optional[int]
        local_system_ip: Optional[str]
        message: Optional[str]
        status: Optional[str]
        trace_id: Optional[int]
        uuid: Optional[str]


    class NwpiTraceStartRespPayload:
        """
        Nwpi trace start response payload schema
        """

        action: Optional[str]
        domain_mon: Optional[bool]
        entry_time: Optional[int]
        expire_time: Optional[int]
        local_drop_rate_threshold: Optional[int]
        qos_mon: Optional[bool]
        source_site: Optional[str]
        state: Optional[str]
        trace_id: Optional[int]
        trace_name: Optional[str]
        traces: Optional[List[NwpiTraceStartRespPayloadTraces]]
        wan_drop_rate_threshold: Optional[int]


    class NwpiTraceStartReqPayload:
        """
        Trace start payload schema
        """

        app: Optional[List[str]]
        app_vis: Optional[str]
        art_vis: Optional[str]
        dia_vis: Optional[str]
        dscp: Optional[str]
        dst_pfx: Optional[str]
        dst_port: Optional[str]
        duration: Optional[str]
        hub_wan_vis: Optional[str]
        protocol: Optional[str]
        sampling: Optional[str]
        source_site: Optional[str]
        spl_intvl: Optional[str]
        src_if: Optional[str]
        src_pfx: Optional[str]
        src_port: Optional[str]
        trace_name: Optional[str]
        vpn_id: Optional[str]


