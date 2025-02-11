======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class ProcessResponse:
        # Procees Id of the task
        id: Optional[str]


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


    class OnRampGatewayConnection:
        """
        Interconnect onRamp gateway connection information
        """

        # Interconnect onRamp gateway connection name
        name: str
        # Interconnect onRamp gateway connection id
        id: Optional[str]


    class VirtualNetworkTagAssociation:
        """
        Interconnect virtual network connection virtual network tag association list
        """

        # Type of resource to be associated to the tag
        resource_type: str
        # Interconnect onRamp gateway connection information
        on_ramp_gateway_connection: Optional[OnRampGatewayConnection]


    class VirtualNetworkTag:
        """
        Interconnect virtual network connection virtual network tag list
        """

        # Name of the Host VPC/VNET tag
        tag_name: str


    class InterconnectVirtualNetworkConnection:
        # Interconnect virtual network connection cloud account id
        cloud_account_id: str
        # Interconnect virtual network connection cloud account name
        cloud_account_name: str
        # Cloud provider type
        cloud_type: str
        # Interconnect  virtual network connection name
        connection_name: str
        # Interconnect virtual network connection tag association type
        virtual_network_tag_association_type: str
        # Interconnect virtual network connection virtual network tag association list
        virtual_network_tag_associations: List[
            VirtualNetworkTagAssociation
        ]
        # Interconnect virtual network connection virtual network tag list
        virtual_network_tags: List[VirtualNetworkTag]
        # Interconnect virtual network connection id
        connection_id: Optional[str]
        # Interconnect virtual network connection resource state information
        resource_state: Optional[InterconnectResourceState]


