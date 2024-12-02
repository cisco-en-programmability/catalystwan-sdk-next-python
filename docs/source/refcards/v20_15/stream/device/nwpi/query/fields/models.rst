======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class QueryFieldsResponsePayloadInner:
        """
        Nwpi Query fields
        """

        data_type: Optional[str]
        is_required: Optional[bool]
        multi_select: Optional[bool]
        name: Optional[str]
        property: Optional[str]
        validation: Optional[Any]


