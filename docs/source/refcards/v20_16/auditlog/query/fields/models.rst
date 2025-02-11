======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class GetStatQueryFieldsFieldData:
        type_: Optional[str]


    class GetStatQueryFieldOptions:
        key: str
        value: str
        enable_date_fields: Optional[bool]
        is_selected: Optional[bool]
        number: Optional[str]


    class GetStatQueryFields:
        data_type: str
        is_required: bool
        multi_select: bool
        name: str
        property: str
        field_data: Optional[GetStatQueryFieldsFieldData]
        options: Optional[List[GetStatQueryFieldOptions]]


