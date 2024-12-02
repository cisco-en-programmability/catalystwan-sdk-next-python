======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    ValueType = Literal[
        "ARRAY", "FALSE", "NULL", "NUMBER", "OBJECT", "STRING", "TRUE"
    ]


    class GetSubscriptions1PostRequest:
        empty: Optional[bool]
        value_type: Optional[ValueType]


