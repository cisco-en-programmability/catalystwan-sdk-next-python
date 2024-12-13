======
Models
======


.. code:: python

    from typing import List, Dict, Union, Literal, Optional, Any

    CloudTypeParam = Literal[
        "AWS", "AWS_GOVCLOUD", "AZURE", "AZURE_GOVCLOUD", "GCP"
    ]


    class TagsResponse:
        tag: Optional[str]


