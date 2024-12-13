======
Models
======


.. code:: python

    from typing import List, Dict, Union, Literal, Optional, Any

    EdgeTypeParam = Literal["EQUINIX", "MEGAPORT"]

    ValueType = Literal[
        "ARRAY", "FALSE", "NULL", "NUMBER", "OBJECT", "STRING", "TRUE"
    ]


    class UpdateIcgwPutRequest:
        empty: Optional[bool]
        value_type: Optional[ValueType]


