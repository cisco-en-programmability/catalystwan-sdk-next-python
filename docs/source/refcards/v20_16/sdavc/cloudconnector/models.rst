======
Models
======


.. code:: python

    from typing import Union, Dict, Optional, Literal, List, Any

    ValueType = Literal[
        "ARRAY", "FALSE", "NULL", "NUMBER", "OBJECT", "STRING", "TRUE"
    ]


    class DisableCloudConnectorPutRequest:
        empty: Optional[bool]
        value_type: Optional[ValueType]


