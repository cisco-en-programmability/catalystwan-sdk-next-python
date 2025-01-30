======
Models
======


.. code:: python

    from typing import Literal, Any, Union, Dict, Optional, List

    CloudTypeParam = Literal[
        "AWS", "AWS_GOVCLOUD", "AZURE", "AZURE_GOVCLOUD", "GCP"
    ]


    class SwImagesResponse:
        device_model: Optional[str]
        display_name: Optional[str]
        is_payg_image: Optional[bool]
        software_image_id: Optional[str]
        version: Optional[str]


