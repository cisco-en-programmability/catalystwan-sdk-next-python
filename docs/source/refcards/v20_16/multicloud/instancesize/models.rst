======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    CloudTypeParam = Literal[
        "AWS", "AWS_GOVCLOUD", "AZURE", "AZURE_GOVCLOUD", "GCP"
    ]


    class InstanceSizeResponse:
        size: Optional[str]
        spec: Optional[str]


