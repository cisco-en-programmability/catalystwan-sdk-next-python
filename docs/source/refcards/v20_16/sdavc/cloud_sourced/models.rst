======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class L3L4:
        clear_index: Optional[int]
        ip_addresses: Optional[List[str]]
        l4_protocol: Optional[str]
        ports: Optional[List[int]]


    class ServerName:
        name: Optional[str]


    class ApplicationDetails:
        app_name: Optional[str]
        application_family: Optional[str]
        application_group: Optional[str]
        business_relevance: Optional[str]
        cloud_sourced: Optional[str]
        common_name: Optional[str]
        id: Optional[str]
        l3_l4: Optional[List[L3L4]]
        server_names: Optional[List[ServerName]]
        source_category: Optional[str]
        status: Optional[str]
        traffic_class: Optional[str]
        uuid: Optional[str]


    class GetExtendedApplicationResponse:
        count: Optional[int]
        data: Optional[List[ApplicationDetails]]
        last_update_on: Optional[int]


    class DefaultSuccessResponse:
        message: Optional[str]
        success: Optional[bool]


    class ApplicationRequestDetails:
        app_name: Optional[str]


    class SaveExtendedApplicationRequest:
        data: Optional[List[ApplicationRequestDetails]]
        select_all: Optional[bool]
        update_network: Optional[bool]


