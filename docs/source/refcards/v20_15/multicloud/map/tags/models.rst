======
Models
======


.. code:: python

    from typing import List, Dict, Optional, Union, Any, Literal

    CloudTypeParam = Literal[
        "AWS", "AWS_GOVCLOUD", "AZURE", "AZURE_GOVCLOUD", "GCP"
    ]


    class TagsResponse:
        tag: Optional[str]


