======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class FlowlogDataObject:
        action: Optional[str]
        dest_ip: Optional[str]
        dest_port: Optional[int]
        device_model: Optional[str]
        direction: Optional[str]
        dscp: Optional[int]
        egress_intf: Optional[str]
        entry_time: Optional[int]
        flow_active: Optional[str]
        host_name: Optional[str]
        ingress_intf: Optional[str]
        ip_proto: Optional[int]
        policy_name: Optional[str]
        src_ip: Optional[str]
        src_port: Optional[int]
        start_time: Optional[int]
        statcycletime: Optional[int]
        stats_data_id: Optional[str]
        tenant: Optional[str]
        total_bytes: Optional[int]
        total_pkts: Optional[int]
        vdevice_name: Optional[str]
        vmanage_system_ip: Optional[str]
        vpn_id: Optional[int]


    class FlowlogPaginationResponsePageInfo:
        count: Optional[int]
        end_time: Optional[str]
        has_more_data: Optional[str]
        scroll_id: Optional[str]
        start_time: Optional[str]
        total_count: Optional[int]


    class FlowlogPaginationResponse:
        data: Optional[List[FlowlogDataObject]]
        page_info: Optional[FlowlogPaginationResponsePageInfo]


