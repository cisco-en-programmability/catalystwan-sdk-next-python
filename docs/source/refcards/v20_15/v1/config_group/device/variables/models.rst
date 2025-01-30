======
Models
======


.. code:: python

    from typing import List, Dict, Optional, Union, Any, Literal

    ValueType = Literal[
        "ARRAY", "FALSE", "NULL", "NUMBER", "OBJECT", "STRING", "TRUE"
    ]


    class CreateConfigGroupDeviceVariablesPutRequest:
        empty: Optional[bool]
        value_type: Optional[ValueType]


