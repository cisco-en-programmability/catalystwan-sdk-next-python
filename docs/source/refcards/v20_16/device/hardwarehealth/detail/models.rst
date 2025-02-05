======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class DeviceHardwareHealthDetail:
        bfd_sessions: Optional[str]
        board_serial: Optional[str]
        control_connections: Optional[str]
        cpu_load_display: Optional[str]
        device_model: Optional[str]
        device_type: Optional[str]
        hardware_state: Optional[str]
        host_name: Optional[str]
        lastupdated: Optional[int]
        local_system_ip: Optional[str]
        mem_usage_display: Optional[str]
        number_vsmart_peers: Optional[int]
        omp_peers: Optional[str]
        reachability: Optional[str]
        site_id: Optional[str]
        system_ip: Optional[str]
        uptime_date: Optional[int]
        uuid: Optional[str]
        version: Optional[str]


