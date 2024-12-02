======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class InterfaceAggResp:
        count: Optional[int]
        entry_time: Optional[str]
        interface: Optional[str]
        rx_kbps: Optional[int]
        tx_kbps: Optional[int]
        vdevice_name: Optional[str]


    class PageInfo:
        # number of alarms to be fetched
        count: Optional[int]
        # end time of alarms to be fetched
        end_time: Optional[int]
        # start time of alarms to be fetched
        start_time: Optional[int]


    class InterfaceAggRespWithPageInfo:
        """
        interface aggregation response with page info
        """

        data: Optional[List[InterfaceAggResp]]
        page_info: Optional[PageInfo]


