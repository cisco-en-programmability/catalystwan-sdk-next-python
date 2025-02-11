======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class InterfaceStatisticsRes:
        admin_status: Optional[str]
        af_type: Optional[str]
        bw_down: Optional[int]
        bw_up: Optional[int]
        device_model: Optional[str]
        down_capacity_percentage: Optional[int]
        entry_time: Optional[int]
        host_name: Optional[str]
        id: Optional[str]
        interface: Optional[str]
        interface_type: Optional[str]
        oper_status: Optional[str]
        platform_type: Optional[str]
        rx_drops: Optional[int]
        rx_errors: Optional[int]
        rx_kbps: Optional[int]
        rx_octets: Optional[int]
        rx_pkts: Optional[int]
        rx_pps: Optional[int]
        statcycletime: Optional[int]
        stats_data_id: Optional[str]
        system_ip: Optional[str]
        tenant: Optional[str]
        total_mbps: Optional[int]
        tx_drops: Optional[int]
        tx_errors: Optional[int]
        tx_kbps: Optional[int]
        tx_octets: Optional[int]
        tx_pkts: Optional[int]
        tx_pps: Optional[int]
        up_capacity_percentage: Optional[int]
        vdevice_name: Optional[str]
        vip_idx: Optional[int]
        vip_time: Optional[int]
        vmanage_system_ip: Optional[str]
        vnf_name: Optional[str]
        vnic_id: Optional[str]
        vpn_id: Optional[int]


