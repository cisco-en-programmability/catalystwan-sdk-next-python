======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class NPingResponse:
        avg_round_trip: Optional[int]
        loss_percentage: Optional[int]
        max_round_trip: Optional[int]
        min_round_trip: Optional[int]
        packets_received: Optional[int]
        packets_transmitted: Optional[int]
        raw_output: Optional[List[str]]


    class NPingRequest:
        count: Optional[str]
        dest_port: Optional[str]
        df: Optional[str]
        host: Optional[str]
        interface_ip: Optional[str]
        mtu: Optional[str]
        probe_type: Optional[str]
        rapid: Optional[str]
        size: Optional[str]
        source: Optional[str]
        source_port: Optional[str]
        tos: Optional[str]
        ttl: Optional[str]
        vpn: Optional[str]


