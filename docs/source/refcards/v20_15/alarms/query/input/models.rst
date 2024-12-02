======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class SimpleKeyValueMapping:
        key: Optional[str]
        value: Optional[str]


    class TimeOptions:
        enable_date_fields: Optional[bool]
        key: Optional[str]
        value: Optional[str]


    class AlarmQueryInputResponse:
        component: Optional[List[SimpleKeyValueMapping]]
        severity_options: Optional[List[SimpleKeyValueMapping]]
        time_options: Optional[List[TimeOptions]]


