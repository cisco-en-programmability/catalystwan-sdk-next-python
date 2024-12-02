======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class CloudGatewayListResponse:
        account_id: Optional[str]
        account_name: Optional[str]
        cloud_gateway_id: Optional[str]
        cloud_gateway_name: Optional[str]
        cloud_type: Optional[str]
        custom_settings: Optional[bool]
        description: Optional[str]
        region: Optional[str]
        status: Optional[str]


    class Taskid:
        """
        Task id for polling status
        """

        id: Optional[str]


    class CloudGatewayPostAzureProperties:
        """
        Used in Azure/Azure GovCloud CGW creation
        """

        resource_group_name: str
        resource_group_source: str
        vhub_name: str
        vhub_source: str
        vwan_name: str
        vwan_source: str
        nva_source: Optional[str]
        vpn_gateway_source: Optional[str]


    class CloudGatewayPostConfigGroupSettings:
        """
        Used in Azure/Azure GovCloud CGW creation
        """

        config_group_id: Optional[str]
        config_group_name: Optional[str]


    class AllOfcloudGatewayPostSettings:
        cloud_gateway_solution: Optional[str]
        cloud_type: Optional[str]
        instance_size: Optional[str]
        ip_subnet_pool: Optional[str]
        name: Optional[str]
        # Used for GCP Custom settings
        network_tier: Optional[str]
        # Used for Azure/Azure GovCloud Custom settings
        sku_scale_unit: Optional[str]
        software_image_id: Optional[str]
        # Tunnel Count for AWS Connect based and branch connect
        tunnel_count: Optional[str]


    class CloudGatewayPost:
        account_id: str
        # Used in Azure/Azure GovCloud CGW creation
        azure_properties: CloudGatewayPostAzureProperties
        cloud_gateway_name: str
        cloud_type: str
        cloud_gateway_mode: Optional[str]
        cloud_gateway_solution: Optional[str]
        cloud_gateway_tag: Optional[str]
        # Used in Azure/Azure GovCloud CGW creation
        config_group_settings: Optional[
            CloudGatewayPostConfigGroupSettings
        ]
        description: Optional[str]
        devices: Optional[List[str]]
        mrf_router_role: Optional[str]
        region: Optional[str]
        s2s_permitted: Optional[str]
        settings: Optional[AllOfcloudGatewayPostSettings]
        site_name: Optional[str]
        ssh_key_name: Optional[str]


    class CustomSettings:
        cloud_gateway_solution: Optional[str]
        cloud_type: Optional[str]
        instance_size: Optional[str]
        ip_subnet_pool: Optional[str]
        name: Optional[str]
        # Used for GCP Custom settings
        network_tier: Optional[str]
        # Used for Azure/Azure GovCloud Custom settings
        sku_scale_unit: Optional[str]
        software_image_id: Optional[str]
        # Tunnel Count for AWS Connect based and branch connect
        tunnel_count: Optional[str]


    class TunnelsInner:
        """
        CGW details relevant to AWS/AWS_GOVCLOUD
        """

        accepted_route_count: Optional[int]
        last_status_change_timestamp: Optional[str]
        outer_ip_addr: Optional[str]
        status: Optional[str]
        status_message: Optional[str]
        tunnel_id: Optional[str]
        tunnel_inner_ip: Optional[List[str]]


    class CloudGatewayAdjusted:
        account_id: Optional[str]
        cloud_gateway_id: Optional[str]
        # Only applicable to AWS/AWS_GOVCLOUD CloudTypes
        cloud_gateway_mode: Optional[str]
        cloud_gateway_name: Optional[str]
        cloud_gateway_solution: Optional[str]
        # CGW details relevant to AWS/AWS_GOVCLOUD
        cloud_provider_asn: Optional[int]
        # CGW details relevant to AWS/AWS_GOVCLOUD
        cloud_provider_mgmt_reference: Optional[str]
        cloud_type: Optional[str]
        connected_sites: Optional[int]
        connectivity_state: Optional[str]
        connectivity_state_update_ts: Optional[int]
        custom_settings: Optional[bool]
        description: Optional[str]
        devices: Optional[List[str]]
        mrf_router_role: Optional[str]
        region: Optional[str]
        # CGW details relevant to AZURE/AZURE_GOVCLOUD CloudTypes
        resource_group_name: Optional[str]
        # CGW details relevant to AWS/AWS_GOVCLOUD
        route_table_count: Optional[str]
        # Only applicable to GCP CloudGateways
        s2s_permitted: Optional[bool]
        settings: Optional[CustomSettings]
        site_name: Optional[str]
        status: Optional[str]
        # CGW details relevant to AWS/AWS_GOVCLOUD
        tunnel_cidr_blocks: Optional[List[Any]]
        # CGW details relevant to AWS/AWS_GOVCLOUD
        tunnels: Optional[List[TunnelsInner]]
        # CGW details relevant to AZURE/AZURE_GOVCLOUD CloudTypes
        vhub_name: Optional[str]
        # CGW details relevant to AZURE/AZURE_GOVCLOUD CloudTypes
        virtual_router_asn: Optional[str]
        vpns: Optional[List[str]]
        # CGW details relevant to AZURE/AZURE_GOVCLOUD CloudTypes
        vwan_name: Optional[str]


    class UpdateCgwDeviceChanges:
        """
        Used for GCP updateCgw
        """

        devices_added: Optional[List[str]]
        devices_deleted: Optional[List[str]]


    class AllOfupdateCgwSettings:
        cloud_gateway_solution: Optional[str]
        cloud_type: Optional[str]
        instance_size: Optional[str]
        ip_subnet_pool: Optional[str]
        name: Optional[str]
        # Used for GCP Custom settings
        network_tier: Optional[str]
        # Used for Azure/Azure GovCloud Custom settings
        sku_scale_unit: Optional[str]
        software_image_id: Optional[str]
        # Tunnel Count for AWS Connect based and branch connect
        tunnel_count: Optional[str]


    class UpdateCgw:
        account_id: str
        cloud_gateway_name: str
        cloud_type: str
        region: str
        # Used for AZURE updateCgw
        resource_group_name: str
        # Used for AZURE updateCgw
        vhub_id: str
        description: Optional[str]
        # Used for GCP updateCgw
        device_changes: Optional[UpdateCgwDeviceChanges]
        # Used for AZURE updateCgw
        devices: Optional[List[str]]
        mrf_router_role: Optional[str]
        # Used for GCP updateCgw
        s2s_permitted: Optional[str]
        settings: Optional[AllOfupdateCgwSettings]


