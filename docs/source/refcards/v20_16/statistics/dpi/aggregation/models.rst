======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class DpiAggregationResponseData:
        count: Optional[int]
        family: Optional[str]
        octets: Optional[int]


    class DpiAggregationResponseHeaderColumns:
        data_type: Optional[str]
        is_display: Optional[bool]
        property: Optional[str]
        title: Optional[str]


    class DpiAggregationResponseHeaderFields:
        data_type: Optional[str]
        property: Optional[str]


    class DpiAggregationResponseHeader:
        columns: Optional[List[DpiAggregationResponseHeaderColumns]]
        fields: Optional[List[DpiAggregationResponseHeaderFields]]
        generated_on: Optional[int]


    class DpiAggregationResponse:
        data: Optional[List[DpiAggregationResponseData]]
        header: Optional[DpiAggregationResponseHeader]


