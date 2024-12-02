======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class CgwResourceResponseDetailsDevices:
        public_ip: Optional[str]
        uuid: Optional[str]


    class CgwResourceResponseDetails:
        devices: Optional[List[CgwResourceResponseDetailsDevices]]
        vhub_name: Optional[str]
        virtual_router_asn: Optional[str]
        vwan_name: Optional[str]


    class CgwResourceResponse:
        creation_date: Optional[str]
        details: Optional[CgwResourceResponseDetails]
        esource_id: Optional[str]
        resource_type: Optional[str]


