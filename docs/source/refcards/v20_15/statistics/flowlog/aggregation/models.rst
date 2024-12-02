======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class FlowlogAggreation:
        count: Optional[int]
        entry_time: Optional[int]


    class FlowlogAggregationResponseHeaderColumns:
        data_type: Optional[str]
        is_display: Optional[bool]
        property: Optional[str]
        title: Optional[str]


    class FlowlogAggregationResponseHeaderFields:
        data_type: Optional[str]
        property: Optional[str]


    class FlowlogAggregationResponseHeader:
        columns: Optional[List[FlowlogAggregationResponseHeaderColumns]]
        fields: Optional[List[FlowlogAggregationResponseHeaderFields]]
        generated_on: Optional[int]


    class FlowlogAggregationResponse:
        data: Optional[FlowlogAggreation]
        entry_time_list: Optional[List[int]]
        header: Optional[FlowlogAggregationResponseHeader]


