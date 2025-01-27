======
Models
======


.. code:: python

    from typing import List, Dict, Optional, Union, Any, Literal

    ValueType = Literal[
        "ARRAY", "FALSE", "NULL", "NUMBER", "OBJECT", "STRING", "TRUE"
    ]


    class DeployPolicyGroupPostRequest:
        empty: Optional[bool]
        value_type: Optional[ValueType]


