======
Models
======


.. code:: python

    from typing import List, Dict, Union, Literal, Optional, Any

    Health = Literal["fair", "good", "n/a", "poor"]

    State = Literal["Down", "Up"]


    class TunnelHealthOverviewEntry:
        health: Optional[Health]
        health_score: Optional[int]
        jitter: Optional[int]
        latency: Optional[int]
        local_color: Optional[str]
        local_system_ip: Optional[str]
        loss_percentage: Optional[int]
        name: Optional[str]
        remote_color: Optional[str]
        remote_system_ip: Optional[str]
        rx_octets: Optional[int]
        state: Optional[State]
        tx_octets: Optional[int]
        vqoe_score: Optional[int]


    class TunnelHealthOverviewDetail:
        fair: Optional[List[TunnelHealthOverviewEntry]]
        good: Optional[List[TunnelHealthOverviewEntry]]
        poor: Optional[List[TunnelHealthOverviewEntry]]


    class TunnelHealthOverviewTotal:
        fair: Optional[int]
        good: Optional[int]
        poor: Optional[int]


    class TunnelHealthOverview:
        detail: Optional[TunnelHealthOverviewDetail]
        total: Optional[TunnelHealthOverviewTotal]


