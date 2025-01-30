======
Models
======


.. code:: python

    from typing import Literal, Any, Union, Dict, Optional, List

    SortOrderParam = Literal["ASC", "Asc", "DESC", "Desc", "asc", "desc"]


    class QoSResp:
        """
        QOS specific response
        """

        device_model: Optional[str]
        drop_in_bytes: Optional[int]
        drop_in_kbps: Optional[int]
        drop_in_pkts: Optional[int]
        drop_in_pps: Optional[int]
        entry_time: Optional[str]
        host_name: Optional[str]
        id: Optional[str]
        interface: Optional[str]
        queue_name: Optional[str]
        queued_bytes: Optional[int]
        queued_bytes_in_kbps: Optional[int]
        queued_pkts: Optional[int]
        red_drop_bytes: Optional[int]
        red_drop_pkts: Optional[int]
        statcycletime: Optional[str]
        tail_drop_bytes: Optional[int]
        tail_drop_pkts: Optional[int]
        tenant: Optional[str]
        time_interval: Optional[int]
        tx_bytes: Optional[int]
        tx_bytes_in_kbps: Optional[int]
        tx_bytes_in_pps: Optional[int]
        tx_pkts: Optional[int]
        vdevice_name: Optional[str]
        vip_idx: Optional[str]
        vip_time: Optional[str]
        vmanage_system_ip: Optional[str]


    class PageInfo:
        # number of alarms to be fetched
        count: Optional[int]
        # end time of alarms to be fetched
        end_time: Optional[int]
        # start time of alarms to be fetched
        start_time: Optional[int]


    class QoSRespWithPageInfo:
        """
        QoS response with page info
        """

        data: Optional[List[QoSResp]]
        page_info: Optional[PageInfo]


