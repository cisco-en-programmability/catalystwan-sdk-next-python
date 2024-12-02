======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    EdgeTypeParam = Literal["EQUINIX", "MEGAPORT"]

    ValueType = Literal[
        "ARRAY", "FALSE", "NULL", "NUMBER", "OBJECT", "STRING", "TRUE"
    ]


    class UpdateIcgwPutRequest:
        empty: Optional[bool]
        value_type: Optional[ValueType]


