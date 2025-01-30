======
Models
======


.. code:: python

    from typing import Literal, Any, Union, Dict, Optional, List

    Health = Literal["fair", "good", "n/a", "poor"]

    State = Literal["Down", "Up"]


    class DeviceHealthEntryItem:
        cpu_load: Optional[int]
        entry_time: Optional[int]
        health: Optional[Health]
        health_score: Optional[int]
        memory_utilization: Optional[int]
        qoe: Optional[int]
        reachability: Optional[str]


    class TunnelHealthData:
        jitter: Optional[int]
        latency: Optional[int]
        loss_percentage: Optional[int]
        rx_octets: Optional[int]
        state: Optional[State]
        tx_octets: Optional[int]
        vqoe_score: Optional[int]


    class TunnelHealthHistoryItem:
        health: Optional[Health]
        health_score: Optional[int]
        history: Optional[List[DeviceHealthEntryItem]]
        local_color: Optional[str]
        local_system_ip: Optional[str]
        name: Optional[str]
        remote_color: Optional[str]
        remote_system_ip: Optional[str]
        summary: Optional[TunnelHealthData]


