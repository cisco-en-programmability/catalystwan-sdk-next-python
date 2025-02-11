======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    CloudType = Literal[
        "AWS", "AWS_GOVCLOUD", "AZURE", "AZURE_GOVCLOUD", "GCP"
    ]

    AssociationAction = Literal[
        "ASSOCIATE", "DISASSOCIATE", "NO_ACTION", "REMOVE_PREFIX_LIST"
    ]

    ConnectionType = Literal["HCONN", "HVIF"]

    VirtualInterfaceType = Literal[
        "ATTACHMENT", "PRIVATE", "PUBLIC", "TRANSIT"
    ]

    PeeringState = Literal["DISABLED", "ENABLED"]

    PeeringType = Literal["PRIVATE", "PUBLIC"]

    ServiceProviderProvisioningState = Literal[
        "DEPROVISIONING", "NOT_PROVISIONED", "PROVISIONED", "PROVISIONING"
    ]

    VirtualNetworkGatewayType = Literal["EXPRESS_ROUTE", "VPN"]

    CloudTypeParam = Literal["AWS"]


    class GatewayAssociationAssociatedGateway:
        """
        Cloud Connectivity Gateway Object
        """

        cloud_account_id: Optional[str]
        cloud_gateway_name: Optional[str]
        cloud_type: Optional[CloudType]
        description: Optional[str]
        gateway_id: Optional[str]
        gateway_name: Optional[str]
        region: Optional[str]


    class GatewayAssociation:
        """
        Generic multicloud gateway association object
        """

        advertised_prefix_list: Optional[List[str]]
        # Cloud Connectivity Gateway Object
        associated_gateway: Optional[GatewayAssociationAssociatedGateway]
        association_action: Optional[AssociationAction]
        association_id: Optional[str]
        association_state: Optional[str]
        state_change_error: Optional[str]


    class AwsDirectConnectGatewayVirtualInterfaceData:
        """
        VIrtual Interface Object
        """

        advertised_prefix_list: Optional[List[str]]
        asn: Optional[int]
        bgp_key: Optional[str]
        customer_ip_address: Optional[str]
        ip_address: Optional[str]
        vlan: Optional[int]


    class AwsDirectConnectGatewayVirtualInterfaceAttachmentList:
        """
        Virtual Interface Object
        """

        attachment_state: Optional[str]
        cloud_type: Optional[CloudType]
        # Id of the private cross connect
        connection_id: Optional[str]
        # Type of AWS connection
        connection_type: Optional[ConnectionType]
        owner_account: Optional[str]
        region: Optional[str]
        state_change_error: Optional[str]
        # VIrtual Interface Object
        virtual_interface_data: Optional[
            AwsDirectConnectGatewayVirtualInterfaceData
        ]
        virtual_interface_id: Optional[str]
        virtual_interface_name: Optional[str]
        virtual_interface_type: Optional[VirtualInterfaceType]


    class AwsDirectConnectGateway:
        """
        AWS Direct Connect Gateway specific Object.
        """

        amazon_side_asn: str
        # List of associated Gateways
        gateway_association_list: Optional[List[GatewayAssociation]]
        owner_account: Optional[str]
        # List of virtual interfaces attached to DxGW
        virtual_interface_attachment_list: Optional[
            List[AwsDirectConnectGatewayVirtualInterfaceAttachmentList]
        ]
        # VPC Tags associated to the Direct Connect Gateway
        vpc_tag_names_for_gateway_associations: Optional[List[str]]


    class AwsVpcAttachments:
        """
        AWS VPC attachment Object
        """

        region: Optional[str]
        # VPC Id
        vpc_id: Optional[str]
        # List of ip prefixes to be advertized towards DxGw on the VPC routing table.
        vpc_route_prefix_list: Optional[List[str]]
        vpc_state: Optional[str]
        # List of VPC subnets to be added to DxGw association.
        vpc_subnet_prefix_list: Optional[List[str]]


    class AwsTransitGateway:
        """
        AWS Transit Gateway specific Object.
        """

        amazon_side_asn: str
        association_default_route_table_id: Optional[str]
        auto_accept_shared_attachments: Optional[bool]
        creation_time: Optional[str]
        default_route_table_association: Optional[bool]
        default_route_table_propogation: Optional[bool]
        dns_support: Optional[bool]
        multicast_support: Optional[bool]
        owner_account: Optional[str]
        propogation_default_route_table_id: Optional[str]
        # List of VPC attachments
        vpc_attachment_list: Optional[List[AwsVpcAttachments]]
        vpn_ecmp_support: Optional[bool]


    class AwsVirtualPrivateGateway:
        """
        AWS Virtual Private Gateway specific Object.
        """

        amazon_side_asn: Optional[int]
        availability_zone: Optional[str]
        # List of VPC attachments
        vpc_attachment_list: Optional[List[AwsVpcAttachments]]
        vpg_type: Optional[str]


    class CloudConnectivityGatewayAws:
        """
        AWS cloud Connectivity Gateway Object
        """

        aws_connectivity_type: str
        # AWS Direct Connect Gateway specific Object.
        direct_connect_gateway: Optional[AwsDirectConnectGateway]
        # AWS Transit Gateway specific Object.
        transit_gateway: Optional[AwsTransitGateway]
        # AWS Virtual Private Gateway specific Object.
        virtual_private_gateway: Optional[AwsVirtualPrivateGateway]


    class AzureErcPeering:
        """
        Azure Express Route Circuit Peering
        """

        advertised_public_prefix_list: Optional[List[str]]
        azure_asn: Optional[str]
        express_route_connection_id: Optional[str]
        id: Optional[str]
        name: Optional[str]
        peer_asn: Optional[str]
        peering_state: Optional[PeeringState]
        peering_type: Optional[PeeringType]
        primary_azure_port: Optional[str]
        primary_peer_address_prefix: Optional[str]
        secondary_azure_port: Optional[str]
        secondary_peer_address_prefix: Optional[str]
        # BGP Peering Key
        shared_key: Optional[str]
        vlan_id: Optional[int]


    class AzureErcServiceProviderProperties:
        """
        Azure Express Route Circuit Service Provider Properties
        """

        bandwidth_in_mbps: Optional[int]
        peering_location: Optional[str]
        service_provider_name: Optional[str]


    class AzureExpressRouteCircuitSku:
        """
        Express Route Circuit SKU
        """

        family: str
        tier: str
        name: Optional[str]


    class AzureVirtualWanTagList:
        """
        Azure Virtual WAN Tag Object
        """

        name: Optional[str]
        value: Optional[str]


    class AzureVirtualHubVirtualRouterIp:
        """
        Virtual Router IP
        """

        private_ip: Optional[str]


    class AzureVirtualHub:
        """
        Azure Virtual Hub
        """

        account_id: Optional[str]
        account_name: Optional[str]
        address_prefix: Optional[str]
        cloud_type: Optional[CloudType]
        id: Optional[str]
        name: Optional[str]
        provisioning_state: Optional[str]
        region: Optional[str]
        resource_group_name: Optional[str]
        routing_state: Optional[str]
        sku: Optional[str]
        tag_list: Optional[List[AzureVirtualWanTagList]]
        virtual_router_asn: Optional[str]
        virtual_router_ip: Optional[List[AzureVirtualHubVirtualRouterIp]]
        vwan_name: Optional[str]


    class AzureExpressRouteCircuitVHubList:
        is_delete: Optional[bool]
        # Azure Virtual Hub
        v_hub: Optional[AzureVirtualHub]


    class AzureVirtualWan:
        """
        Azure Virtual Wan
        """

        name: str
        region: str
        resource_group_name: str
        account_id: Optional[str]
        # Cloud account name
        account_name: Optional[str]
        allow_branch_to_branch_traffic: Optional[bool]
        cloud_type: Optional[str]
        description: Optional[str]
        id: Optional[str]
        provisioning_state: Optional[str]
        tag_list: Optional[List[AzureVirtualWanTagList]]
        virtual_wan_type: Optional[str]
        vnet_tovnet_traffic_enabled: Optional[bool]


    class AzureExpressRouteCircuitVWanAttachmentList:
        """
        vWan Attachment Name
        """

        v_hub_list: Optional[List[AzureExpressRouteCircuitVHubList]]
        # Azure Virtual Wan
        v_wan: Optional[AzureVirtualWan]


    class AzureExpressRouteCircuitVnetTagNamesForConnections:
        """
        Vnet Tag Object Names
        """

        is_delete: Optional[bool]
        vnet_tag_name: Optional[str]


    class AzureExpressRouteCircuit:
        """
        Azure Express Route Circuit Object
        """

        resource_group_name: str
        allow_classic_operations: Optional[bool]
        bandwidth_in_gbps: Optional[int]
        gateway_association_list: Optional[List[GatewayAssociation]]
        global_reach_enabled: Optional[bool]
        peering_list: Optional[List[AzureErcPeering]]
        provisioning_state: Optional[str]
        service_key: Optional[str]
        # Azure Express Route Circuit Service Provider Properties
        service_provider_properties: Optional[
            AzureErcServiceProviderProperties
        ]
        service_provider_provisioning_state: Optional[
            ServiceProviderProvisioningState
        ]
        # Express Route Circuit SKU
        sku: Optional[AzureExpressRouteCircuitSku]
        v_wan_attachment_list: Optional[
            List[AzureExpressRouteCircuitVWanAttachmentList]
        ]
        vnet_tag_names_for_connections: Optional[
            List[AzureExpressRouteCircuitVnetTagNamesForConnections]
        ]


    class AzureExpressRouteGateway:
        """
        Azure Express Route Gateway Object
        """

        auto_scale_configuration: Optional[str]
        resource_group_name: Optional[str]
        # Id of the Azure vHUB.
        v_hub_id: Optional[str]


    class AzureVirtualNetworkGatewaySku:
        """
        VNET Gateway SKU parameters
        """

        capacity: Optional[int]
        name: Optional[str]
        tier: Optional[str]


    class AzureVirtualNetworkGateway:
        """
        Azure Virtual Network Gateway Object
        """

        enable_bgp: Optional[bool]
        public_ip_address: Optional[str]
        # VNET Gateway SKU parameters
        sku: Optional[AzureVirtualNetworkGatewaySku]
        subnet: Optional[str]
        virtual_network_gateway_type: Optional[VirtualNetworkGatewayType]


    class CloudConnectivityGatewayAzure:
        """
        Cloud Connectivity Gateway Object
        """

        azure_connectivity_type: str
        # Azure Express Route Circuit Object
        express_route_circuit: Optional[AzureExpressRouteCircuit]
        # Azure Express Route Gateway Object
        express_route_gateway: Optional[AzureExpressRouteGateway]
        # Azure Virtual Network Gateway Object
        virtual_network_gateway: Optional[AzureVirtualNetworkGateway]


    class GcpInterconnectAttachment:
        """
        Google cloud Interconnect Attachment Object.
        """

        cloud_router_ip_address: Optional[str]
        customer_ip_address: Optional[str]
        id: Optional[str]
        # MTU of the Interconnect attachment
        mtu: Optional[str]
        name: Optional[str]
        pairing_key: Optional[str]
        region: Optional[str]
        # Option to create Interconnect attachment in secondary zone
        secondary_zone: Optional[str]
        state: Optional[str]


    class GcpCloudRouter:
        """
        Google cloud GCR Object.
        """

        name: str
        network: str
        # List of GCR Attachments
        attachment_details: Optional[List[GcpInterconnectAttachment]]
        cloud_router_asn: Optional[str]
        id: Optional[str]
        region: Optional[str]


    class CloudConnectivityGatewayGcp:
        """
        Google cloud Connectivity Gateway Object.
        """

        gc_connectivity_type: str
        # Google cloud GCR Object.
        router_info: GcpCloudRouter
        # BGP ASN assigned to Interconnect Gateway.
        interconnect_asn: Optional[str]
        pairing_key: Optional[str]


    class CloudConnectivityGateway:
        """
        Cloud Connectivity Gateway Object
        """

        # AWS cloud Connectivity Gateway Object
        aws_connectivity_gateway: CloudConnectivityGatewayAws
        # Cloud Connectivity Gateway Object
        azure_connectivity_gateway: CloudConnectivityGatewayAzure
        cloud_account_id: str
        cloud_type: str
        gateway_name: str
        # Google cloud Connectivity Gateway Object.
        gcp_connectivity_gateway: CloudConnectivityGatewayGcp
        region: str
        cloud_gateway_name: Optional[str]
        connectivity_gateway_state: Optional[str]
        description: Optional[str]
        gateway_id: Optional[str]
        # Resource created by vManage
        is_vmanage_created: Optional[bool]
        # Option indicates object type
        new_format: Optional[bool]


    class InlineResponse2008:
        """
        Cloud Connectivity Gateway Object
        """

        connectivity_gateway: Optional[List[CloudConnectivityGateway]]


