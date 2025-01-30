======
Models
======


.. code:: python

    from typing import List, Dict, Optional, Union, Any, Literal

    SortOrderParam = Literal["ASC", "Asc", "DESC", "Desc", "asc", "desc"]


    class RuleTypes:
        field: Optional[str]
        operator: Optional[str]
        type_: Optional[str]
        value: Optional[List[str]]


    class QueryWithRule:
        condition: Optional[str]
        rules: Optional[RuleTypes]


    class InterfaceQuery:
        query: Optional[QueryWithRule]


    class InterfaceResp:
        """
        interface specific response
        """

        device_model: Optional[str]
        dst_ip: Optional[str]
        dst_port: Optional[int]
        entry_time: Optional[str]
        fec_re: Optional[int]
        fec_rx: Optional[int]
        fec_tx: Optional[int]
        host_name: Optional[str]
        id: Optional[str]
        jitter: Optional[int]
        latency: Optional[int]
        local_color: Optional[str]
        local_system_ip: Optional[str]
        loss: Optional[int]
        loss_percentage: Optional[int]
        name: Optional[str]
        proto: Optional[str]
        remote_color: Optional[str]
        remote_system_ip: Optional[str]
        rx_octets: Optional[int]
        rx_pkts: Optional[int]
        sla_class_list: Optional[str]
        sla_class_names: Optional[str]
        src_ip: Optional[str]
        src_port: Optional[int]
        statcycletime: Optional[str]
        state: Optional[str]
        tenant: Optional[str]
        total: Optional[int]
        tunnel_color: Optional[str]
        tx_octets: Optional[int]
        tx_pkts: Optional[int]
        vdevice_name: Optional[str]
        vip_idx: Optional[int]
        vmanage_system_ip: Optional[str]
        vqoe_score: Optional[int]


    class PageInfo:
        # number of alarms to be fetched
        count: Optional[int]
        # end time of alarms to be fetched
        end_time: Optional[int]
        # start time of alarms to be fetched
        start_time: Optional[int]


    class InterfaceRespWithPageInfo:
        """
        interface response with page info
        """

        data: Optional[List[InterfaceResp]]
        page_info: Optional[PageInfo]


