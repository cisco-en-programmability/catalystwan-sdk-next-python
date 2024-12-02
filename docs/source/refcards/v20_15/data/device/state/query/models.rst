======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class GenerateDeviceStateDataData:
        _rid: Optional[int]
        auto_downstream_bandwidth: Optional[str]
        auto_upstream_bandwidth: Optional[str]
        bia_address: Optional[str]
        create_time_stamp: Optional[str]
        description: Optional[str]
        hwaddr: Optional[str]
        if_admin_status: Optional[str]
        if_oper_status: Optional[str]
        ifindex: Optional[str]
        ifname: Optional[str]
        interface_type: Optional[str]
        ip_address: Optional[str]
        ipv4_subnet_mask: Optional[str]
        ipv4_tcp_adjust_mss: Optional[str]
        ipv6_tcp_adjust_mss: Optional[str]
        lastupdated: Optional[int]
        mtu: Optional[str]
        record_id: Optional[str]
        rx_drops: Optional[int]
        rx_errors: Optional[int]
        rx_octets: Optional[int]
        rx_packets: Optional[str]
        speed_mbps: Optional[str]
        tx_drops: Optional[int]
        tx_errors: Optional[int]
        tx_octets: Optional[int]
        tx_packets: Optional[int]
        vdevice_data_key: Optional[str]
        vdevice_host_name: Optional[str]
        vdevice_name: Optional[str]
        vmanage_system_ip: Optional[str]
        vpn_id: Optional[str]


    class GenerateDeviceStateDataWithQueryString:
        data: Optional[List[GenerateDeviceStateDataData]]


