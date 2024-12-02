======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class FlowInfoResponseDataDownstreamDeviceList:
        device_name: Optional[str]
        device_system_ip: Optional[str]
        local_color: Optional[str]
        remote_color: Optional[str]


    class FlowInfoResponseDataDownstreamHopList:
        art: Optional[str]
        asymmetry_detected: Optional[bool]
        dpi_policy_used: Optional[bool]
        fif_dpi_not_classified: Optional[bool]


    class FlowInfoResponseDataUpstreamDeviceList:
        device_name: Optional[str]
        device_system_ip: Optional[str]
        ingress_pre_invalid: Optional[bool]


    class FlowInfoResponseDataUpstreamHopList:
        art: Optional[str]
        asymmetry_detected: Optional[bool]
        dpi_policy_used: Optional[bool]


    class FlowInfoResponseData:
        app_group: Optional[str]
        app_name: Optional[str]
        appqoe_diverted: Optional[bool]
        art: Optional[str]
        asymmetry_detected: Optional[bool]
        big_drop: Optional[bool]
        big_wan_drop: Optional[bool]
        device_trace_id: Optional[int]
        domain: Optional[List[str]]
        domain_name: Optional[str]
        domain_src: Optional[str]
        downstream_device_list: Optional[
            List[FlowInfoResponseDataDownstreamDeviceList]
        ]
        downstream_dscp: Optional[str]
        downstream_hop_list: Optional[
            FlowInfoResponseDataDownstreamHopList
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
        flow_readout: Optional[Any]
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
        timestamp: Optional[int]
        upstream_device_list: Optional[
            List[FlowInfoResponseDataUpstreamDeviceList]
        ]
        upstream_dscp: Optional[str]
        upstream_hop_list: Optional[
            List[FlowInfoResponseDataUpstreamHopList]
        ]
        utd_diverted: Optional[bool]
        vpn_id: Optional[str]
        wan_color_asym: Optional[bool]


    class ActiveFlowResponsePayload:
        """
        Active flows data response payload
        """

        data: Optional[List[FlowInfoResponseData]]


