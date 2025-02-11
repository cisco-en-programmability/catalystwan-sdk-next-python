======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class PingResponse:
        avg_round_trip: Optional[int]
        loss_percentage: Optional[int]
        max_round_trip: Optional[int]
        min_round_trip: Optional[int]
        packets_received: Optional[int]
        packets_transmitted: Optional[int]
        raw_output: Optional[List[str]]


    class PingRequest:
        count: Optional[str]
        host: Optional[str]
        rapid: Optional[str]
        size: Optional[str]
        source: Optional[str]
        vpn: Optional[str]


