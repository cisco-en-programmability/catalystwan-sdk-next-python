======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    CloudTypeParam = Literal[
        "AWS", "AWS_GOVCLOUD", "AZURE", "AZURE_GOVCLOUD", "GCP"
    ]


    class InstanceSizeResponse:
        size: Optional[str]
        spec: Optional[str]


