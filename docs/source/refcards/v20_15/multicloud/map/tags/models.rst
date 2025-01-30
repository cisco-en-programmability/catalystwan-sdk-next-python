======
Models
======


.. code:: python

    from typing import Literal, Any, Union, Dict, Optional, List

    CloudTypeParam = Literal[
        "AWS", "AWS_GOVCLOUD", "AZURE", "AZURE_GOVCLOUD", "GCP"
    ]


    class TagsResponse:
        tag: Optional[str]


