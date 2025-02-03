======
Models
======


.. code:: python

    from typing import Any, List, Dict, Literal, Optional, Union

    CloudTypeParam = Literal[
        "AWS", "AWS_GOVCLOUD", "AZURE", "AZURE_GOVCLOUD", "GCP"
    ]


    class GetRegions:
        cloud_type: Optional[str]
        region_list: Optional[str]


