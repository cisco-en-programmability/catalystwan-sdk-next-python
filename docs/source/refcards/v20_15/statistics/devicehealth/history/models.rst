======
Models
======


.. code:: python

    from typing import Literal, Any, Union, Dict, Optional, List

    Health = Literal["fair", "good", "n/a", "poor"]


    class DeviceHealthEntryItem:
        cpu_load: Optional[int]
        entry_time: Optional[int]
        health: Optional[Health]
        health_score: Optional[int]
        memory_utilization: Optional[int]
        qoe: Optional[int]
        reachability: Optional[str]


    class DeviceHealthHistoryItem:
        cpu_load: Optional[int]
        health: Optional[Health]
        health_score: Optional[int]
        history: Optional[List[DeviceHealthEntryItem]]
        host_name: Optional[str]
        memory_utilization: Optional[int]
        qoe: Optional[int]
        reachability: Optional[str]
        site_id: Optional[str]
        system_ip: Optional[str]


