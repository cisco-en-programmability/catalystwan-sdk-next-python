======
Models
======


.. code:: python

    from typing import Union, Dict, Optional, Literal, List, Any

    CloudTypeParam = Literal[
        "AWS", "AWS_GOVCLOUD", "AZURE", "AZURE_GOVCLOUD", "GCP"
    ]


    class TagsResponse:
        tag: Optional[str]


