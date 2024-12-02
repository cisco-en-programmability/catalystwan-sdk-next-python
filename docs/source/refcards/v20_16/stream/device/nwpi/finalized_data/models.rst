======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class NwpitraceFlowRespPayloadDataDownstreamDeviceList:
        device_name: Optional[str]
        device_system_ip: Optional[str]
        down_fwd_decision: Optional[str]
        egress_next_invalid: Optional[bool]
        local_color: Optional[str]
        remote_color: Optional[str]
        up_fwd_decision: Optional[str]


    class NwpitraceFlowRespPayloadDataDownstreamHopList:
        appqoe_diverted: Optional[bool]
        art: Optional[str]
        asymmetry_detected: Optional[bool]
        big_drop: Optional[bool]
        big_wan_drop: Optional[bool]
        dpi_policy_used: Optional[bool]
        fif_dpi_not_classified: Optional[bool]
        flow_id: Optional[int]
        his_q_d_avg_pkts: Optional[int]
        his_q_d_max_pkts: Optional[int]
        his_q_d_min_pkts: Optional[int]
        hop_index: Optional[int]
        jitter: Optional[str]
        latency: Optional[str]
        local_color: Optional[str]
        local_drop_cause_num: Optional[int]
        local_drop_rate: Optional[str]
        local_edge: Optional[str]
        local_system_ip: Optional[str]
        nat_translated: Optional[bool]
        path_changed: Optional[bool]
        policy_bypassed: Optional[bool]
        q_d_avg_pkts: Optional[int]
        q_d_max_pkts: Optional[int]
        q_d_min_pkts: Optional[int]
        q_id: Optional[int]
        q_lim_pkts: Optional[int]
        qos_congested: Optional[bool]
        remote_color: Optional[str]
        remote_drop_cause_num: Optional[int]
        remote_drop_rate: Optional[str]
        remote_edge: Optional[str]
        remote_system_ip: Optional[str]
        server_no_response: Optional[bool]
        sla_violated: Optional[bool]
        sla_violated_bfd: Optional[bool]
        tcp_flow_reset: Optional[bool]
        total_bytes: Optional[str]
        total_packets: Optional[str]
        utd_diverted: Optional[bool]
        wan_color_asym: Optional[bool]
        wan_drop_rate: Optional[str]
        wan_drop_str: Optional[str]


    class NwpitraceFlowRespPayloadDataFlowReadout:
        application: Optional[str]
        flow_last_update_time: Optional[str]
        flow_start_time: Optional[str]
        total_flow_num_counted: Optional[bool]
        total_flow_num_last15_mins_counted: Optional[bool]


    class NwpitraceFlowRespPayloadDataUpActualPath:
        interface: Optional[str]
        type: Optional[str]


    class NwpitraceFlowRespPayloadDataUpstreamDeviceList:
        device_name: Optional[str]
        device_system_ip: Optional[str]
        down_actual_path: Optional[
            NwpitraceFlowRespPayloadDataUpActualPath
        ]
        down_fwd_decision: Optional[str]
        egress_next_invalid: Optional[bool]
        ingress_pre_invalid: Optional[bool]
        local_color: Optional[str]
        remote_color: Optional[str]
        up_actual_path: Optional[NwpitraceFlowRespPayloadDataUpActualPath]
        up_fwd_decision: Optional[str]


    class NwpitraceFlowRespPayloadData:
        app_group: Optional[str]
        app_name: Optional[str]
        appqoe_diverted: Optional[bool]
        art: Optional[str]
        asymmetry_detected: Optional[bool]
        big_drop: Optional[bool]
        big_wan_drop: Optional[bool]
        device_trace_id: Optional[int]
        domain_name: Optional[str]
        domain_src: Optional[str]
        downstream_device_list: Optional[
            List[NwpitraceFlowRespPayloadDataDownstreamDeviceList]
        ]
        downstream_dscp: Optional[str]
        downstream_hop_list: Optional[
            List[NwpitraceFlowRespPayloadDataDownstreamHopList]
        ]
        dpi_policy_used: Optional[bool]
        dst_ip: Optional[str]
        dst_port: Optional[int]
        dst_sgt: Optional[str]
        fif_dpi_not_classified: Optional[bool]
        flow_fin: Optional[bool]
        flow_id: Optional[int]
        flow_key: Optional[str]
        flow_moved: Optional[bool]
        flow_readout: Optional[NwpitraceFlowRespPayloadDataFlowReadout]
        max_local_drop_rate: Optional[int]
        max_wan_drop_rate: Optional[int]
        nat_translated: Optional[bool]
        path_changed: Optional[bool]
        policy_bypassed: Optional[bool]
        protocol: Optional[str]
        qos_congested: Optional[bool]
        received_timestamp: Optional[int]
        server_no_response: Optional[bool]
        sla_violated: Optional[bool]
        sla_violated_bfd: Optional[bool]
        src_ip: Optional[str]
        src_port: Optional[int]
        src_sgt: Optional[str]
        start_device: Optional[str]
        start_timestamp: Optional[int]
        tcp_flow_reset: Optional[bool]
        test_id: Optional[int]
        timestamp: Optional[int]
        upstream_device_list: Optional[
            List[NwpitraceFlowRespPayloadDataUpstreamDeviceList]
        ]
        upstream_dscp: Optional[str]
        upstream_hop_list: Optional[
            List[NwpitraceFlowRespPayloadDataDownstreamHopList]
        ]
        user_group: Optional[str]
        user_name: Optional[str]
        utd_diverted: Optional[bool]
        vpn_id: Optional[str]
        wan_color_asym: Optional[bool]


    class NwpitraceFlowRespPayloadData1:
        data: Optional[NwpitraceFlowRespPayloadData]
        entry_time: Optional[int]
        tenant: Optional[str]
        trace_id: Optional[int]
        type_: Optional[str]


    class NwpitraceFlowRespPayload:
        """
        Nwpi traceFlow response payload schema
        """

        data: Optional[List[NwpitraceFlowRespPayloadData1]]


