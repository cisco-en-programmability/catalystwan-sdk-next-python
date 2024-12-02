======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class CustomSettings:
        cloud_gateway_solution: Optional[str]
        cloud_type: Optional[str]
        instance_size: Optional[str]
        ip_subnet_pool: Optional[str]
        name: Optional[str]
        # Used for GCP Custom settings
        network_tier: Optional[str]
        # Used for Azure/Azure GovCloud Custom settings
        sku_scale_unit: Optional[str]
        software_image_id: Optional[str]
        # Tunnel Count for AWS Connect based and branch connect
        tunnel_count: Optional[str]


