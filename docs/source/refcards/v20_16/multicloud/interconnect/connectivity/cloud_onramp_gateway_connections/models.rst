======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    ValueType = Literal[
        "ARRAY", "FALSE", "NULL", "NUMBER", "OBJECT", "STRING", "TRUE"
    ]


    class DirectConnectGatewayDetails:
        """
        Interconnect OnRamp gateway connection Direct connect gateway details
        """

        # Interconnect OnRamp AWS Direct Connect Gateway cloud resource id
        cloud_resource_id: str
        # Interconnect On Ramp AWS Direct Connect Gateway cloud resource id
        id: Optional[str]
        # Interconnect On Ramp AWS Direct Connect Gateway cloud resource name
        name: Optional[str]


    class ExpressRouteCircuitDetails:
        """
        Interconnect OnRamp gateway connection Express route circuit details
        """

        # Interconnect OnRamp Azure express route circuit cloud resource id
        cloud_resource_id: str
        # Interconnect OnRamp Azure express route circuit id
        id: Optional[str]
        # Interconnect OnRamp Azure express route circuit name
        name: Optional[str]
        # Interconnect OnRamp Azure express route circuit resource group
        resource_group_name: Optional[str]
        # Interconnect OnRamp Azure express route circuit service key
        service_key: Optional[str]


    class CgwDetails:
        """
        Interconnect OnRamp gateway association MultiCloud gateway details
        """

        # Interconnect On Ramp Gateway connection cloud connect cloud account id
        cloud_account_id: str
        # Interconnect OnRamp gateway associated cgw gateway name
        name: str
        # Interconnect on ramp gateway connection cgw advertised prefixes
        advertised_prefixes: Optional[List[str]]
        # Interconnect OnRamp gateway associated cgw gateway id
        id: Optional[str]


    class TgwDetails:
        """
        Interconnect OnRamp gateway association Transit gateway details
        """

        # Prefixes to be advertised to the Direct Connect Gateway
        advertised_prefixes: List[str]
        # Transit gateway cloud account id
        cloud_account_id: str
        # Transit gateway create flag
        is_create: str
        # Transit Gateway cloud side BGP ASN
        bgp_asn: Optional[str]
        # Transit gateway cloud resource id
        cloud_resource_id: Optional[str]
        create: Optional[bool]
        # Transit gateway id
        id: Optional[str]
        # Transit gateway name
        name: Optional[str]
        # Transit gateway region
        region: Optional[str]


    class VhubDetails:
        """
        Interconnect OnRamp gateway association Virtual hub details
        """

        # Virtual hub gateway address prefix
        address_prefix: str
        # Virtual hub gateway cloud account id
        cloud_account_id: str
        # Virtual hub gateway create flag
        is_create: str
        # Virtual hub gateway cloud resource id
        cloud_resource_id: Optional[str]
        create: Optional[bool]
        # Virtual hub gateway id
        id: Optional[str]
        # Virtual hub gateway name
        name: Optional[str]
        # Virtual hub gateway region
        region: Optional[str]
        # Virtual hub gateway resource group
        resource_group_name: Optional[str]


    class GatewayAssociationDetail:
        """
        Interconnect OnRamp gateway connection gateway associations
        """

        # Interconnect OnRamp gateway association type
        resource_type: str
        # Interconnect OnRamp gateway association MultiCloud gateway details
        cgw_details: Optional[CgwDetails]
        # Interconnect OnRamp gateway association Transit gateway details
        tgw_details: Optional[TgwDetails]
        # Interconnect OnRamp gateway association Virtual hub details
        vhub_details: Optional[VhubDetails]


    class GoogleCloudRouterDetails:
        """
        Interconnect OnRamp gateway connection Google cloud router details
        """

        # Interconnect OnRamp Google cloud router & attachment cloud resource id
        cloud_resource_id: str
        # Interconnect OnRamp Google cloud router & attachment role
        role: str
        # Interconnect OnRamp Google cloud router attachment detail
        google_attachment_detail: Optional[str]
        # Interconnect OnRamp Google cloud router id
        id: Optional[str]
        # Interconnect OnRamp Google cloud router name
        name: Optional[str]
        # Interconnect OnRamp Google cloud router network
        network: Optional[str]
        # Interconnect OnRamp Google cloud router region
        region: Optional[str]


    class ConnectionDetail:
        """
        Interconnect cross connection attachment connection details
        """

        # Interconnect cross connection name
        connection_name: str


    class InterconnectAttachments:
        """
        Interconnect OnRamp gateway connection interconnect attachments
        """

        # Interconnect cross connection attachment resource type
        resource_type: str
        # Interconnect cross connection attachment connection details
        connection_details: Optional[ConnectionDetail]


    class ResourceAssociationDetail:
        associated_resource_connection_status: Optional[str]
        associated_resource_id: Optional[str]
        associated_resource_name: Optional[str]
        associated_resource_status: Optional[str]


    class InterconnectResourceState:
        """
        Interconnect virtual network connection resource state information
        """

        resource_association_details: Optional[
            List[ResourceAssociationDetail]
        ]
        resource_state: Optional[str]
        resource_state_message: Optional[str]
        resource_state_update_ts: Optional[str]


    class VirtualWanDetails:
        """
        Interconnect OnRamp gateway connection Azure virtual wan details
        """

        # Interconnect OnRamp Azure virtual wan cloud resource id
        cloud_resource_id: str
        # Interconnect OnRamp Azure virtual wan id
        id: Optional[str]
        # Interconnect OnRamp Azure virtual wan name
        name: Optional[str]
        # Interconnect OnRamp Azure virtual wan resource group
        resource_group_name: Optional[str]


    class InterconnectOnRampGatewayConnection:
        # Interconnect cloud connect cloud access type
        cloud_access_type: str
        # Interconnect OnRamp gateway connection cloud connect cloud account id
        cloud_account_id: str
        # Interconnect OnRamp gateway connection cloud connect cloud account id
        cloud_account_name: str
        # Interconnect OnRamp gateway connection cloud connect cloud provider type
        cloud_type: str
        # Interconnect OnRamp gateway connection id
        connection_id: str
        # Interconnect OnRamp gateway connection name
        connection_name: str
        # Interconnect OnRamp gateway optional description
        description: Optional[str]
        # Interconnect OnRamp gateway connection Direct connect gateway details
        direct_connect_gateway_details: Optional[
            DirectConnectGatewayDetails
        ]
        # Interconnect OnRamp gateway connection Express route circuit details
        express_route_circuit_details: Optional[
            ExpressRouteCircuitDetails
        ]
        # Interconnect OnRamp gateway connection gateway associations
        gateway_associations: Optional[List[GatewayAssociationDetail]]
        # Interconnect OnRamp gateway connection Google cloud router details
        google_cloud_router_details: Optional[
            List[GoogleCloudRouterDetails]
        ]
        # Interconnect OnRamp gateway connection interconnect attachments
        interconnect_attachments: Optional[List[InterconnectAttachments]]
        # Interconnect virtual network connection resource state information
        interconnect_resource_state: Optional[InterconnectResourceState]
        # Interconnect cloud connect cloud access type
        on_ramp_gateway_type: Optional[str]
        # Interconnect cloud connect virtual network association type
        virtual_network_association_type: Optional[str]
        # Interconnect OnRamp gateway connection Azure virtual wan details
        virtual_wan_details: Optional[VirtualWanDetails]


    class CreateInterconnectOnRampGatewayConnectionPostRequest:
        value_type: Optional[ValueType]


    class ProcessResponse:
        # Procees Id of the task
        id: Optional[str]


    class UpdateInterconnectOnRampGatewayConnectionPutRequest:
        empty: Optional[bool]
        value_type: Optional[ValueType]


