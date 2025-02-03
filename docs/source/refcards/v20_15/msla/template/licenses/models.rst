======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    ValueType = Literal[
        "ARRAY", "FALSE", "NULL", "NUMBER", "OBJECT", "STRING", "TRUE"
    ]


    class GetSubscriptions1PostRequest:
        empty: Optional[bool]
        value_type: Optional[ValueType]


