======
Models
======


.. code:: python

    from typing import Literal, Any, Union, Dict, Optional, List

    ValueType = Literal[
        "ARRAY", "FALSE", "NULL", "NUMBER", "OBJECT", "STRING", "TRUE"
    ]


    class SubmitDay0ConfigPostRequest:
        empty: Optional[bool]
        value_type: Optional[ValueType]


