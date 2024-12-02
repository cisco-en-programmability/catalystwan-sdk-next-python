======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class NwpipacketRespPayloadDataPacketPacketEgressFia:
        feature_detail: Optional[str]
        feature_name: Optional[str]
        fia_color: Optional[str]
        policy_key: Optional[str]


    class NwpipacketRespPayloadDataPacketPacket:
        egress_fia: Optional[
            List[NwpipacketRespPayloadDataPacketPacketEgressFia]
        ]
        ingress_fia: Optional[
            List[NwpipacketRespPayloadDataPacketPacketEgressFia]
        ]


    class NwpipacketRespPayloadDataPacket:
        app_awared: Optional[bool]
        event_name: Optional[List[str]]
        packet: Optional[NwpipacketRespPayloadDataPacketPacket]
        packet_fwd_decision: Optional[str]
        packet_id: Optional[int]
        parent_pkt_id: Optional[int]


    class NwpipacketRespPayloadData:
        device_name: Optional[str]
        device_version: Optional[str]
        flow_id: Optional[int]
        packet: Optional[NwpipacketRespPayloadDataPacket]
        packet_received_timestamp: Optional[int]
        system_ip: Optional[str]
        trace_id: Optional[int]


    class NwpipacketRespPayloadData1:
        data: Optional[NwpipacketRespPayloadData]
        entry_time: Optional[int]
        tenant: Optional[str]
        trace_id: Optional[int]
        type_: Optional[str]


    class NwpipacketRespPayload:
        """
        Nwpi trace packet payload schema
        """

        data: Optional[List[NwpipacketRespPayloadData1]]


