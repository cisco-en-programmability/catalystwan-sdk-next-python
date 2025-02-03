======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    ValueType = Literal[
        "ARRAY", "FALSE", "NULL", "NUMBER", "OBJECT", "STRING", "TRUE"
    ]


    class SubmitDay0ConfigPostRequest:
        empty: Optional[bool]
        value_type: Optional[ValueType]


