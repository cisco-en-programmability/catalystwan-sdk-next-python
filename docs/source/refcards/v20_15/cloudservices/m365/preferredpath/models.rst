======
Models
======


.. code:: python

    from typing import List, Dict, Optional, Union, Any, Literal

    ValueType = Literal[
        "ARRAY", "FALSE", "NULL", "NUMBER", "OBJECT", "STRING", "TRUE"
    ]


    class GetO365PreferredPathFromVAnalyticsPostRequest:
        empty: Optional[bool]
        value_type: Optional[ValueType]


