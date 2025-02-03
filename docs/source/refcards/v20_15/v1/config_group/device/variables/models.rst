======
Models
======


.. code:: python

    from typing import Any, Union, List, Dict, Optional, Literal

    ValueType = Literal[
        "ARRAY", "FALSE", "NULL", "NUMBER", "OBJECT", "STRING", "TRUE"
    ]


    class CreateConfigGroupDeviceVariablesPutRequest:
        empty: Optional[bool]
        value_type: Optional[ValueType]


