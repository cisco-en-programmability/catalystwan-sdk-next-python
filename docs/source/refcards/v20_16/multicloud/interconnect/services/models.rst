======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class InterconnectService:
        # Virtual Instance flavor of the service instance
        flavor: Optional[str]
        # Number of interfaces for the service
        interface_count: Optional[str]
        # IP of the management interface of the service
        mgmt_ip: Optional[str]
        # Name of the service
        name: Optional[str]
        # Region where the service is deployed
        service_region: Optional[str]
        # HA role of the service
        service_role: Optional[str]
        # Status of the service
        status: Optional[str]
        # Software version running on the service
        sw_version: Optional[str]
        # provider assigned service Uuid
        uuid: Optional[str]


