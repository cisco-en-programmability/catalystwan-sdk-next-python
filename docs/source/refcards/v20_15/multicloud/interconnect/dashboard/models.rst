======
Models
======


.. code:: python

    from typing import Literal, Optional, List, Union, Dict, Any

    EdgeType = Literal["EQUINIX", "MEGAPORT"]


    class InterconnectDashboardConnections:
        connectivity_name: Optional[str]
        resource_state: Optional[str]


    class InterconnectDashboardLinkList:
        device_link_name: Optional[str]
        resource_state: Optional[str]


    class InterconnectDashboard:
        connections: Optional[List[InterconnectDashboardConnections]]
        devices: Optional[List[str]]
        edge_account_id: Optional[str]
        edge_account_name: Optional[str]
        edge_gateway_id: Optional[str]
        edge_gateway_name: Optional[str]
        edge_type: Optional[EdgeType]
        link_list: Optional[List[InterconnectDashboardLinkList]]
        region: Optional[str]
        resource_state: Optional[str]
        resource_state_update_ts: Optional[str]


