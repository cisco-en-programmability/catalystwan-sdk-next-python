======
Models
======


.. code:: python

    from typing import Any, Union, List, Dict, Optional, Literal

    Severity = Literal["CRITICAL", "MAJOR", "MEDIUM", "MINOR"]


    class AlarmAggregation:
        count: Optional[int]
        entry_time: Optional[int]
        severity: Optional[Severity]


    class AlarmAggregationResponse:
        data: Optional[AlarmAggregation]
        entry_time_list: Optional[List[int]]


