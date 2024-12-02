======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    CloudTypeParam = Literal[
        "AWS", "AWS_GOVCLOUD", "AZURE", "AZURE_GOVCLOUD", "GCP"
    ]


    class CloudGatewayListResponse:
        account_id: Optional[str]
        account_name: Optional[str]
        cloud_gateway_id: Optional[str]
        cloud_gateway_name: Optional[str]
        cloud_type: Optional[str]
        custom_settings: Optional[bool]
        description: Optional[str]
        region: Optional[str]
        status: Optional[str]


