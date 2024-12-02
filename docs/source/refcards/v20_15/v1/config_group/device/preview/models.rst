======
Models
======


.. code:: python

    from typing import Literal, Optional, List, Union, Dict, Any

    ValueType = Literal[
        "ARRAY", "FALSE", "NULL", "NUMBER", "OBJECT", "STRING", "TRUE"
    ]


    class GetConfigGroupDeviceConfigurationPreviewPostRequest:
        empty: Optional[bool]
        value_type: Optional[ValueType]


