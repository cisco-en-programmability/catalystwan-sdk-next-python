======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class AppRouteAggResp:
        count: Optional[int]
        entry_time: Optional[str]
        local_color: Optional[str]
        loss_percentage: Optional[int]


    class PageInfo:
        # number of alarms to be fetched
        count: Optional[int]
        # end time of alarms to be fetched
        end_time: Optional[int]
        # start time of alarms to be fetched
        start_time: Optional[int]


    class AppRouteAggRespWithPageInfo:
        """
        interface aggregation response with page info
        """

        data: Optional[List[AppRouteAggResp]]
        page_info: Optional[PageInfo]


