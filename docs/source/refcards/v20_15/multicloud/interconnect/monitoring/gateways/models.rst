======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class InterconnectGatewayMonitoring:
        device_uuid: str
        edge_account_id: str
        edge_gateway_name: str
        edge_type: str
        region: str
        site_name: str
        description: Optional[str]
        edge_account_name: Optional[str]
        edge_gateway_id: Optional[str]
        # Custom Settings enabled for Interconnect Gateway
        is_custom_setting: Optional[bool]
        resource_state: Optional[str]
        status: Optional[str]


