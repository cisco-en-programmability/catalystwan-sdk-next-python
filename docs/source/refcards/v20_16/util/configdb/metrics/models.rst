======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class MetricData:
        # timestamp in seconds
        time: Optional[str]
        # count/value for corresponding timestamp
        value: Optional[str]


    class Neo4JMetricsResponse:
        data: Optional[List[MetricData]]
        # limit given in reqeust. By default - 500
        limit: Optional[int]
        # Page Number given in request. By default - 1
        page_no: Optional[int]
        # Records present on the current page
        records_current_page: Optional[int]
        # Total Pages calculates based on limit and totalRecords values
        total_pages: Optional[int]
        # Total count of metrics records ignoring limit
        total_records: Optional[int]


