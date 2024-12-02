======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class CapacityRespData:
        avg_down_capacity_percentage: Optional[int]
        avg_up_capacity_percentage: Optional[int]
        bw_down: Optional[int]
        bw_up: Optional[int]
        count: Optional[int]
        interface: Optional[str]
        max_down_capacity_percentage: Optional[int]
        max_up_capacity_percentage: Optional[int]
        min_down_capacity_percentage: Optional[int]
        min_up_capacity_percentage: Optional[int]
        range: Optional[str]
        vdevice_name: Optional[str]


    class CapDistribution:
        s_0_25: Optional[int]
        s_100: Optional[int]
        s_25_50: Optional[int]
        s_50_75: Optional[int]
        s_75_100: Optional[int]
        uncategorized: Optional[int]


    class CapacityResp:
        data: Optional[List[CapacityRespData]]
        distribution: Optional[CapDistribution]


