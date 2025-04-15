======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    ValueType = Literal[
        "ARRAY", "FALSE", "NULL", "NUMBER", "OBJECT", "STRING", "TRUE"
    ]


    class GetPolicyGroupDeviceConfigurationPreviewPostResponse:
        """
        Policy Group preview Response schema
        """

        existing_config: str
        new_config: str
        unsupported_parcels: Optional[List[Any]]


    class GetPolicyGroupDeviceConfigurationPreviewPostRequest:
        empty: Optional[bool]
        value_type: Optional[ValueType]


