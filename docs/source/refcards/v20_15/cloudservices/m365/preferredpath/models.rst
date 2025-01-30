======
Models
======


.. code:: python

    from typing import Literal, Any, Union, Dict, Optional, List

    ValueType = Literal[
        "ARRAY", "FALSE", "NULL", "NUMBER", "OBJECT", "STRING", "TRUE"
    ]


    class GetO365PreferredPathFromVAnalyticsPostRequest:
        empty: Optional[bool]
        value_type: Optional[ValueType]


