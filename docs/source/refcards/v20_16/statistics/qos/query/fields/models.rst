======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class QoSQueryFieldsRespFieldData:
        type_: Optional[str]


    class QueryFieldsOption:
        enabled_date_fields: Optional[bool]
        key: Optional[str]
        number: Optional[str]
        value: Optional[str]


    class QoSQueryFieldsResp:
        data_type: Optional[str]
        field_data: Optional[QoSQueryFieldsRespFieldData]
        is_required: Optional[bool]
        name: Optional[str]
        options: Optional[List[QueryFieldsOption]]
        property: Optional[str]


