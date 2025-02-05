======
Models
======


.. code:: python

    from typing import Union, Dict, Optional, Literal, List, Any

    CloudTypeParam = Literal[
        "AWS", "AWS_GOVCLOUD", "AZURE", "AZURE_GOVCLOUD", "GCP"
    ]


    class GetRegions:
        cloud_type: Optional[str]
        region_list: Optional[str]


