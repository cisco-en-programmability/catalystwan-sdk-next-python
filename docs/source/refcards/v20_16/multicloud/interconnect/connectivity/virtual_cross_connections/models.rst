======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class ProcessResponse:
        # Procees Id of the task
        id: Optional[str]


    class AwsCloudDetail:
        """
        Interconnect cloud connect AWS cloud detail
        """

        # Interconnect cloud connect AWS cloud account id
        cloud_account_id: str
        # Interconnect cloud connect cloud account name
        cloud_account_name: str
        # Interconnect cloud connect AWS cross connect type
        cross_connect_type: str
        # Interconnect cloud connect AWS cloud side BGP ASN
        cloud_side_bgp_asn: Optional[str]
        # Interconnect cloud connect AWS hosted connection id
        hosted_connection_id: Optional[str]
        # Interconnect cloud connect AWS hosted virtual interface id
        virtual_interface_id: Optional[str]


    class AzureCloudDetail:
        """
        Interconnect cloud connect Azure cloud detail
        """

        # Interconnect cloud connect Azure cloud account id
        cloud_account_id: str
        # Interconnect cloud connect cloud account name
        cloud_account_name: str
        # Interconnect cloud connect Azure cross connect type
        cross_connect_type: str
        # Interconnect cloud connect Azure Express Route Circuit service key
        service_key: str


    class GatewayDetail:
        """
        Interconnect connection end gateway detail
        """

        # Interconnect gateway name
        name: str
        # Interconnect gateway id
        id: Optional[str]
        # Interconnect gateway owner account id
        owner_id: Optional[str]
        # Interconnect gateway region name
        region: Optional[str]
        # Interconnect gateway region id
        region_id: Optional[str]


    class InterconnectInterfaceDetail:
        """
        Interconnect connection end interface detail
        """

        # BGP ASN of the connection end
        bgp_asn: Optional[str]
        # BGP key of the connection end
        bgp_key: Optional[str]
        # Interface name of the connection end
        interface_name: Optional[str]
        # Interface IP address of the connection end
        ip_address: Optional[str]
        # MTU of the connection end
        mtu: Optional[str]
        # Interface IP address prefix of the connection end
        prefix: Optional[str]
        # VLAN ID of the connection end
        vlan_id: Optional[str]


    class PortDetail:
        """
        Interconnect connection end port detail
        """

        # Interconnect connection port id
        id: str
        # Interconnect connection port name
        name: str
        # Interconnect connection port owner account id
        owner_id: str
        # Interconnect connection port region name
        region: str
        # Interconnect connection port region id
        region_id: str


    class ConnectionEndDetail:
        """
        Interconnect device connect connection destination
        """

        # Interconnect connection end resource type
        resource_type: str
        # Interconnect connection end gateway detail
        gateway_detail: Optional[GatewayDetail]
        # Interconnect connection end interface detail
        interface_detail: Optional[InterconnectInterfaceDetail]
        # Interconnect connection end port detail
        port_detail: Optional[PortDetail]


    class GoogleCloudDetail:
        """
        Interconnect cloud connect Google cloud detail
        """

        # Interconnect cloud connect cloud account name
        cloud_account_name: str
        # Google cross connect type
        cross_connect_type: str
        # Google GCR attachment pairing key
        pairing_key: str
        # Google cloud account id
        cloud_account_id: Optional[str]


    class CustomPeeringDetails:
        """
        Custom peering information for Interconnect cross connection destination
        """

        # Custom BGP ASN for a connection end
        bgp_asn: Optional[str]
        # Custom ip address for a connection end
        ip_address: Optional[str]
        # Custom ip address prefix for a connection end
        prefix: Optional[str]


    class CustomPeeringInfo:
        """
        Interconnect cross connection custom peering information
        """

        # Custom prefixes to be advertised to cloud for public connections
        advertised_prefixes: Optional[List[str]]
        # Custom peering information for Interconnect cross connection destination
        destination_end: Optional[CustomPeeringDetails]
        # Custom peering information for Interconnect cross connection destination
        source_end: Optional[CustomPeeringDetails]


    class InterconnectCrossConnectionPeeringInfo:
        """
        Interconnect device connect peering information
        """

        # Interconnect cross connection peering type
        peering_type: str
        # Interconnect cross connection peering VPN segment
        vpn_segment: str
        # Interconnect cross connection custom peering information
        custom_peering_info: Optional[CustomPeeringInfo]


    class CloudConnectDetail:
        """
        Interconnect cross connection cloud connection detail
        """

        # Interconnect cloud connect cloud access type
        cloud_access_type: str
        # Interconnect cloud connect cloud provider type
        cloud_type: str
        # Interconnect device connect connection destination
        connection_destination: ConnectionEndDetail
        # Interconnect device connect connection destination
        connection_source: ConnectionEndDetail
        # Interconnect device connect peering information
        peering_info: InterconnectCrossConnectionPeeringInfo
        # Interconnect cloud connect AWS cloud detail
        aws_cloud_detail: Optional[AwsCloudDetail]
        # Interconnect cloud connect Azure cloud detail
        azure_cloud_detail: Optional[AzureCloudDetail]
        # Interconnect cloud connect Google cloud detail
        google_cloud_detail: Optional[GoogleCloudDetail]
        # Interconnect cloud connect virtual network association type
        virtual_network_association_type: Optional[str]


    class DeviceConnectDetail:
        """
        Interconnect cross connection device connection detail
        """

        # Interconnect device connect connection destination
        connection_destination: ConnectionEndDetail
        # Interconnect device connect connection destination
        connection_source: ConnectionEndDetail
        # Interconnect device connect peering information
        peering_info: InterconnectCrossConnectionPeeringInfo


    class InterconnectCrossConnectionLicenseDetail:
        """
        Interconnect cross connection license information
        """

        aws_hc_sku_end_date: Optional[str]
        aws_hc_sku_id: Optional[str]
        end_date: Optional[str]
        max_licensed_bandwidth: Optional[str]
        sku_id: Optional[str]


    class RedundancyInfo:
        """
        Interconnect cross connection redundancy information
        """

        # Interconnect cross connection pair name
        connection_pair_name: str
        # Interconnect cross connection pair id
        connection_pair_id: Optional[str]


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


    class InterconnectCrossConnection:
        # Interconnect cross connection id
        connection_id: str
        # Interconnect cross connection name
        connection_name: str
        # Interconnect cross connection role
        connection_role: str
        # Interconnect connectivity bandwidth
        connection_speed: str
        # Interconnect cross connection type
        connection_type: str
        # Interconnect account id
        interconnect_account_id: str
        # Interconnect provider type
        interconnect_type: str
        # Interconnect cross connection cloud connection detail
        cloud_connect_detail: Optional[CloudConnectDetail]
        # Interconnect cross connection device connection detail
        device_connect_detail: Optional[DeviceConnectDetail]
        # Interconnect cross connection license information
        license_detail: Optional[InterconnectCrossConnectionLicenseDetail]
        # Interconnect cross connection license type
        license_type: Optional[str]
        # Interconnect cross connection redundancy information
        redundancy_info: Optional[RedundancyInfo]
        # Interconnect virtual network connection resource state information
        resource_state: Optional[InterconnectResourceState]


