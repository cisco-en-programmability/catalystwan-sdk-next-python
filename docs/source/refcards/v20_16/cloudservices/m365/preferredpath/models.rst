======
Models
======


.. code:: python

    from typing import Union, Dict, Optional, Literal, List, Any

    ValueType = Literal[
        "ARRAY", "FALSE", "NULL", "NUMBER", "OBJECT", "STRING", "TRUE"
    ]


    class GetO365PreferredPathFromVAnalyticsPostRequest:
        empty: Optional[bool]
        value_type: Optional[ValueType]


