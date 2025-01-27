======
Models
======


.. code:: python

    from typing import List, Dict, Optional, Union, Any, Literal

    EdgeGatewaySolution = Literal["MVE", "NE"]

    EdgeType = Literal["ATT", "EQUINIX", "MEGAPORT"]


    class InterconnectGatewaySettings:
        instance_size: str
        software_image_id: str
        edge_gateway_solution: Optional[EdgeGatewaySolution]
        edge_type: Optional[EdgeType]
        # Assigned name of the Interconnect Gateway Custom Settings
        egw_custom_setting_name: Optional[str]
        # Ip subnet pool assigned to the gateway
        ip_subnet_pool: Optional[str]


