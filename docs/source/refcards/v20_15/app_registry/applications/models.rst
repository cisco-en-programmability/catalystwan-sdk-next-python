======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    ValueType = Literal[
        "ARRAY", "FALSE", "NULL", "NUMBER", "OBJECT", "STRING", "TRUE"
    ]


    class EditAppDetailsPutRequest:
        value_type: Optional[ValueType]


    class PayloadItems:
        _rid: str
        business_relevance: str
        common_family: str
        common_family_display: str
        common_name: str
        common_name_display: str
        nbar_family: str
        nbar_name: str
        qosmos_family: str
        qosmos_name: str
        traffic_class: str
        uuid: str


