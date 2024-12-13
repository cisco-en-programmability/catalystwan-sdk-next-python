======
Models
======


.. code:: python

    from typing import List, Dict, Union, Literal, Optional, Any

    EdgeGatewaySolution = Literal["MVE", "NE"]

    EdgeType = Literal["EQUINIX", "MEGAPORT"]


    class StatusObject:
        count: Optional[int]
        message: Optional[str]
        name: Optional[str]
        status: Optional[str]


    class GwDeviceStatus:
        count: Optional[int]
        name: Optional[str]
        status_list: Optional[List[StatusObject]]
        unreachable_count: Optional[int]


    class GwSiteStatus:
        count: Optional[int]
        name: Optional[str]
        status_list: Optional[List[StatusObject]]


    class GwStatus:
        count: Optional[int]
        name: Optional[str]
        status_list: Optional[List[StatusObject]]


    class InterconnectWidget:
        edge_gateway_solution: Optional[EdgeGatewaySolution]
        edge_type: Optional[EdgeType]
        gw_device_site_ids: Optional[List[int]]
        gw_device_status: Optional[GwDeviceStatus]
        gw_sitestatus: Optional[GwSiteStatus]
        gw_status: Optional[GwStatus]
        num_accounts: Optional[int]
        num_conn: Optional[int]
        num_sdwan_tunnels: Optional[int]


