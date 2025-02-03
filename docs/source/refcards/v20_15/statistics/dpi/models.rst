======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    SortOrderParam = Literal["ASC", "Asc", "DESC", "Desc", "asc", "desc"]


    class DpiDataObject:
        application: Optional[str]
        create_time: Optional[int]
        dest_ip: Optional[str]
        dest_port: Optional[int]
        device_model: Optional[str]
        entry_time: Optional[int]
        expire_time: Optional[int]
        family: Optional[str]
        host_name: Optional[str]
        ip_proto: Optional[int]
        octets: Optional[int]
        packets: Optional[int]
        source_ip: Optional[str]
        source_port: Optional[int]
        vdevice_name: Optional[str]
        vip_idx: Optional[int]
        vpn_id: Optional[int]


    class DpiResponsePageInfo:
        count: Optional[int]
        end_time: Optional[str]
        start_time: Optional[str]


    class DpiResponse:
        data: Optional[List[DpiDataObject]]
        page_info: Optional[DpiResponsePageInfo]


