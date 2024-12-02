======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class TraceInfoResponsePayloadSummary:
        agg_client_prefix: Optional[str]
        agg_src_sgt: Optional[str]
        agg_svr_prefix: Optional[str]
        app: Optional[str]
        app_grp: Optional[str]
        app_vis: Optional[str]
        art_vis: Optional[str]
        common_app: Optional[str]
        device_ip: Optional[str]
        dia_vis: Optional[str]
        domain_mon: Optional[str]
        dscp: Optional[str]
        dst_ip: Optional[str]
        dst_pfx: Optional[str]
        dst_pfx_len: Optional[str]
        dst_port: Optional[str]
        duration: Optional[str]
        hub_wan_vis: Optional[str]
        local_drop_rate_threshold: Optional[int]
        message: Optional[str]
        protocol: Optional[str]
        qos_mon: Optional[str]
        sampling: Optional[str]
        source_site: Optional[str]
        source_site_vmanage_version: Optional[str]
        spl_intvl: Optional[str]
        src_if: Optional[str]
        src_ip: Optional[str]
        src_pfx: Optional[str]
        src_pfx_len: Optional[str]
        src_port: Optional[str]
        state: Optional[str]
        stop_time: Optional[int]
        task_id: Optional[int]
        trace_name: Optional[str]
        trace_trigger_event: Optional[str]
        vpn_id: Optional[str]
        vpn_list: Optional[str]
        wan_drop_rate_threshold: Optional[int]
        warning: Optional[str]


    class TraceInfoResponsePayload:
        """
        Trace base info Data Response schema
        """

        entry_time: Optional[int]
        summary: Optional[TraceInfoResponsePayloadSummary]
        trace_id: Optional[int]


