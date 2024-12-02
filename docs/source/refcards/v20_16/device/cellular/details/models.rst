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


    class CellularPageInfo:
        details: Optional[List[CellularDeviceDetail]]


    class CellularDetail:
        page_info: Optional[CellularPageInfo]


