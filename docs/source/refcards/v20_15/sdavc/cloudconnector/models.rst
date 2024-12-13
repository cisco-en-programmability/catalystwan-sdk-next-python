======
Models
======


.. code:: python

    from typing import List, Dict, Union, Literal, Optional, Any

    ValueType = Literal[
        "ARRAY", "FALSE", "NULL", "NUMBER", "OBJECT", "STRING", "TRUE"
    ]


    class DisableCloudConnectorPutRequest:
        empty: Optional[bool]
        value_type: Optional[ValueType]


