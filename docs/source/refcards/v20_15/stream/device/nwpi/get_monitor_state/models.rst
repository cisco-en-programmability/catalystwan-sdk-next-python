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


    class NwpiDomainMonitorStateRespPayload:
        """
        Nwpi get MonitorState response payload
        """

        device_list: Optional[
            List[NwpiDomainMonitorStateRespPayloadDevicelist]
        ]
        entry_time: Optional[str]
        message: Optional[str]
        monitor_state: Optional[str]
        trace_id: Optional[int]


