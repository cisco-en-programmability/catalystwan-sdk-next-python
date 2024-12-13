======
Models
======


.. code:: python

    from typing import List, Dict, Union, Literal, Optional, Any

    CloudTypeParam = Literal[
        "AWS", "AWS_GOVCLOUD", "AZURE", "AZURE_GOVCLOUD", "GCP"
    ]


    class MapDefaults:
        conn: Optional[str]
        conn_type: Optional[str]
        dest_type: Optional[str]
        editable: Optional[bool]
        src_type: Optional[str]


