======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class NwpiDomainMonitorStateRespPayloadDevicelist:
        app_vis: Optional[str]
        art_vis: Optional[str]
        connected_v_manages: Optional[str]
        device_ip: Optional[str]
        device_type: Optional[str]
        dia_vis: Optional[str]
        domain_mon: Optional[str]
        domain_monitor_can_be_started: Optional[str]
        dscp_is_valid: Optional[str]
        duration: Optional[str]
        entry_time: Optional[int]
        expire_time: Optional[int]
        local_system_ip: Optional[str]
        message: Optional[str]
        parent_trace_id: Optional[int]
        qos_mon: Optional[str]
        site_id: Optional[str]
        source_site: Optional[str]
        state: Optional[str]
        trace_id: Optional[int]
        trace_name: Optional[str]
        uuid: Optional[str]
        version: Optional[str]
        vpn_id: Optional[str]


    class NwpiTraceHistoryRespPayloadDataSummary:
        agg_client_prefix: Optional[str]
        agg_src_sgt: Optional[str]
        agg_svr_prefix: Optional[str]
        agg_user_name: Optional[str]
        app: Optional[str]
        app_grp: Optional[str]
        app_vis: Optional[str]
        art_vis: Optional[str]
        common_app: Optional[str]
        device_ip: Optional[str]
        devices_check_info: Optional[str]
        dia_vis: Optional[str]
        domain_mon: Optional[str]
        dscp: Optional[str]
        dst_ip: Optional[str]
        dst_pfx: Optional[str]
        dst_pfx_len: Optional[str]
        dst_port: Optional[str]
        duration: Optional[str]
        health_app_server_mem: Optional[str]
        health_cpu_core: Optional[str]
        health_cpu_load: Optional[str]
        health_cpu_load_average: Optional[str]
        health_mem_usage: Optional[str]
        health_running_traces: Optional[int]
        health_server_ip: Optional[str]
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
        trace_stop_type: Optional[str]
        trace_trigger_event: Optional[str]
        username: Optional[str]
        vpn_id: Optional[str]
        vpn_list: Optional[str]
        wan_drop_rate_threshold: Optional[int]
        warning: Optional[str]


    class NwpiTraceHistoryRespPayloadData:
        devices: Optional[
            List[NwpiDomainMonitorStateRespPayloadDevicelist]
        ]
        summary: Optional[NwpiTraceHistoryRespPayloadDataSummary]


    class TaskTracesResponsePayloadInner:
        data: Optional[NwpiTraceHistoryRespPayloadData]
        entry_time: Optional[int]
        tenant: Optional[str]
        trace_id: Optional[int]
        type_: Optional[str]


    class TaskTracesResponsePayload:
        """
        Auto on task schema for GET response
        """

        data: Optional[List[TaskTracesResponsePayloadInner]]


