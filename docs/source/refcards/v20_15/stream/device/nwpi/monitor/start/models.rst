======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class NwpiMonitorRespPayload:
        """
        Nwpi monitor response payload schema
        """

        message: Optional[str]
        monitor_state: Optional[str]


    class NwpiMonitorReqPayloadMapping:
        domain_id: Optional[int]
        uuid: Optional[str]


    class NwpiMonitorReqPayloadDeviceToDomainId:
        domain: Optional[str]
        mapping: Optional[List[NwpiMonitorReqPayloadMapping]]


    class NwpiMonitorReqPayloadDomainList:
        domain: Optional[str]
        resolved_ip: Optional[List[str]]


    class NwpiMonitorReqPayload:
        """
        Nwpi monitor payload schema
        """

        client_ip: Optional[str]
        device_to_domain_id: Optional[
            List[NwpiMonitorReqPayloadDeviceToDomainId]
        ]
        domain_app_grp: Optional[str]
        domain_app_vis: Optional[str]
        domain_list: Optional[List[NwpiMonitorReqPayloadDomainList]]
        trace_id: Optional[str]


