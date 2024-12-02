======
Models
======


.. code:: python

    from typing import Literal, Optional, List, Union, Dict, Any

    ValueType = Literal[
        "ARRAY", "FALSE", "NULL", "NUMBER", "OBJECT", "STRING", "TRUE"
    ]


    class DeployPolicyGroupPostRequest:
        empty: Optional[bool]
        value_type: Optional[ValueType]


