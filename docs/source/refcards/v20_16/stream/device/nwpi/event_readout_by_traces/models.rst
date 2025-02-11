======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class EventReadoutsResponsePayloadDropSendPkts:
        drop_pkts: Optional[int]
        event: Optional[str]
        send_pkts: Optional[int]


    class EventReadoutsResponsePayloadTimeInfo:
        end_time: Optional[str]
        event_num: Optional[str]
        start_time: Optional[str]


    class EventReadoutsResponsePayloadEventHopTimeInfo:
        event_hop: Optional[str]
        event_hop_with_edge: Optional[str]
        time_info: Optional[List[EventReadoutsResponsePayloadTimeInfo]]


    class EventReadoutsResponsePayloadDropCauses:
        drop_cause: Optional[str]


    class EventReadoutsResponsePayloadHopStatistics:
        drop_causes: Optional[
            List[EventReadoutsResponsePayloadDropCauses]
        ]
        event_num: Optional[str]
        hop: Optional[str]
        hop_with_edge: Optional[str]


    class EventReadoutsResponsePayloadEventHopStatistics:
        event: Optional[str]
        hop_statistics: Optional[
            List[EventReadoutsResponsePayloadHopStatistics]
        ]


    class EventReadoutsResponsePayloadEventImpactedFlowNum:
        event: Optional[str]
        impacted_flow_num: Optional[str]


    class EventReadoutsResponsePayloadEventNum:
        event: Optional[str]
        event_num: Optional[str]


    class EventReadoutsResponsePayloadDetail:
        application: Optional[str]
        drop_send_pkts: Optional[
            List[EventReadoutsResponsePayloadDropSendPkts]
        ]
        event_hop_policy_info: Optional[
            List[EventReadoutsResponsePayloadEventHopTimeInfo]
        ]
        event_hop_statistics: Optional[
            List[EventReadoutsResponsePayloadEventHopStatistics]
        ]
        event_hop_time_info: Optional[
            List[EventReadoutsResponsePayloadEventHopTimeInfo]
        ]
        event_impacted_flow_num: Optional[
            List[EventReadoutsResponsePayloadEventImpactedFlowNum]
        ]
        event_list: Optional[List[str]]
        event_num: Optional[List[EventReadoutsResponsePayloadEventNum]]
        total_flow_num: Optional[int]


    class EventReadoutsResponsePayloadData:
        app: Optional[str]
        app_grp: Optional[str]
        app_vis: Optional[str]
        art_vis: Optional[str]
        common_app: Optional[str]
        detail: Optional[List[EventReadoutsResponsePayloadDetail]]
        device_ip: Optional[str]
        dia_vis: Optional[str]
        domain_mon: Optional[str]
        dscp: Optional[str]
        dst_ip: Optional[str]
        dst_pfx: Optional[str]
        dst_pfx_len: Optional[str]
        dst_port: Optional[str]
        duration: Optional[str]
        entry_time: Optional[int]
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
        trace_id: Optional[int]
        trace_name: Optional[str]
        vpn_id: Optional[str]
        wan_drop_rate_threshold: Optional[int]
        warning: Optional[str]


