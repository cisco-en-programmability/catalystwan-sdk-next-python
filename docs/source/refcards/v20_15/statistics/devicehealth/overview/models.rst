======
Models
======


.. code:: python

    from typing import Literal, Any, Union, Dict, Optional, List

    Health = Literal["fair", "good", "n/a", "poor"]

    PersonalityParam = Literal["vbond", "vedge", "vmanage", "vsmart"]


    class DeviceHealthDetailItem:
        cpu_load: int
        health: Health  # pytype: disable=annotation-type-mismatch
        health_score: int
        host_name: str
        memory_utilization: int
        qoe: int
        reachability: str
        site_id: str
        system_ip: str


    class DeviceHealthOverviewDetail:
        fair: Optional[List[DeviceHealthDetailItem]]
        good: Optional[List[DeviceHealthDetailItem]]
        poor: Optional[List[DeviceHealthDetailItem]]


    class DeviceHealthOverviewTotal:
        fair: Optional[int]
        good: Optional[int]
        poor: Optional[int]


    class DeviceHealthOverview:
        detail: Optional[DeviceHealthOverviewDetail]
        total: Optional[DeviceHealthOverviewTotal]


