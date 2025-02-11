======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    LastNHoursParam = Literal["1", "12", "24", "3", "6"]


    class CellularDeviceDetail:
        active_sim: Optional[str]
        carrier: Optional[str]
        device_type: Optional[str]
        host_name: Optional[str]
        if_name: Optional[str]
        link_up_time: Optional[str]
        local_system_ip: Optional[str]
        model: Optional[str]
        product: Optional[str]
        rat: Optional[str]
        slot: Optional[str]
        system_ip: Optional[str]
        total_kbs: Optional[int]
        uuid: Optional[str]


    class CellularDataUsageDetailsItem:
        carrier_name: Optional[str]
        device_list: Optional[List[CellularDeviceDetail]]
        total_usage: Optional[int]


    class CellularDataUsageDetails:
        carrier_name: Optional[str]
        device_list: Optional[List[CellularDeviceDetail]]
        month_usage: Optional[CellularDataUsageDetailsItem]
        one_day_usage: Optional[CellularDataUsageDetailsItem]
        three_month_usage: Optional[CellularDataUsageDetailsItem]
        total_usage: Optional[int]
        week_usage: Optional[CellularDataUsageDetailsItem]


    class CellularDataUsageBasicItem:
        carrier_name: Optional[str]
        total_usage: Optional[int]


    class CellularDataUsage:
        carrier_name: Optional[CellularDataUsageDetails]
        details: Optional[List[CellularDataUsageBasicItem]]


