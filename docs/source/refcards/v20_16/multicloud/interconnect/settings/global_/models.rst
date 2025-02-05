======
Models
======


.. code:: python

    from typing import Union, Dict, Optional, Literal, List, Any

    InterconnectTypeParam = Literal["EQUINIX", "MEGAPORT"]


    class MulticloudSystemSettings:
        enable_monitoring: Optional[bool]
        # Enable or disable Configuration Group for Gateways
        use_configuration_group: Optional[str]


    class InterconnectGlobalSettings:
        bgp_asn: str
        edge_gateway_solution: str
        edge_type: str
        instance_size: str
        loopback_cgw_color: str
        loopback_tunnel_color: str
        software_image_id: str
        invoice_reference: Optional[str]
        ip_subnet_pool: Optional[str]
        multicloud_system_settings: Optional[MulticloudSystemSettings]


