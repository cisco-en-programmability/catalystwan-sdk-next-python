======
Models
======


.. code:: python

    from typing import Any, List, Dict, Literal, Optional, Union

    ConnectivityGatewayTypeParam = Literal[
        "DIRECT_CONNECT_GATEWAY",
        "EXPRESS_ROUTE_CIRCUIT",
        "GCR_ATTACHMENT",
        "TRANSIT_GATEWAY",
        "VIRTUAL_INTERFACES",
        "VIRTUAL_PRIVATE_GATEWAY",
    ]


    class InlineResponse20014CreationOptionsExpressRouteCircuitServiceProviderList:
        bandwidths_offered: Optional[List[int]]
        id: Optional[str]
        location: Optional[str]
        name: Optional[str]
        peering_locations: Optional[List[str]]
        # Provisioning state of the resource
        provisioning_state: Optional[str]
        # Type of Resource
        type_: Optional[str]


    class InlineResponse20014CreationOptionsResourceGroupList:
        id: Optional[str]
        location: Optional[str]
        name: Optional[str]


    class InlineResponse20014CreationOptions:
        express_route_circuit_service_provider_list: Optional[
            List[
                InlineResponse20014CreationOptionsExpressRouteCircuitServiceProviderList
            ]
        ]
        resource_group_list: Optional[
            List[InlineResponse20014CreationOptionsResourceGroupList]
        ]


    class InlineResponse20014:
        creation_options: Optional[InlineResponse20014CreationOptions]


