======
Models
======


.. code:: python

    from typing import Any, Union, List, Dict, Optional, Literal

    LicenseType = Literal["DIRECT", "PAYG", "PREPAID"]

    EdgeGatewaySolution = Literal["MVE", "NE"]

    EdgeType = Literal["ATT", "EQUINIX", "MEGAPORT"]

    InterconnectTypeParam = Literal["EQUINIX", "MEGAPORT"]


    class InterconnectConfigGroupSettings:
        # Config Group Id
        config_group_id: str
        # Config Group name
        config_group_name: str


    class InterconnectMrfSettings:
        # Multi Region Fabric router role
        mrf_router_role: Optional[str]
        # Multi Region Fabric Transport Gateway
        mrf_transport_gateway: Optional[bool]
        # Network Hierarchy Region Id
        nhm_region_id: Optional[int]
        # Network Hierarchy Region name
        nhm_region_name: Optional[str]


    class InterconnectGatewaySettings:
        instance_size: str
        software_image_id: str
        edge_gateway_solution: Optional[EdgeGatewaySolution]
        edge_type: Optional[EdgeType]
        # Assigned name of the Interconnect Gateway Custom Settings
        egw_custom_setting_name: Optional[str]
        # Ip subnet pool assigned to the gateway
        ip_subnet_pool: Optional[str]


    class InterconnectGatewayExtended:
        device_uuid: str
        edge_account_id: str
        edge_billing_account_id: str
        edge_gateway_name: str
        edge_type: str
        ip_transit: str
        license_type: LicenseType
        region: str
        region_id: str
        site_name: str
        config_group_settings: Optional[InterconnectConfigGroupSettings]
        description: Optional[str]
        # BGP ASN assigned to Interconnect Gateway
        egw_bgp_asn: Optional[str]
        ip_transit_id: Optional[str]
        ip_transit_sku_id: Optional[str]
        # Custom Settings enabled for Interconnect Gateway
        is_custom_setting: Optional[bool]
        # License Sku Id of Interconnect Gateway
        license_sku_id: Optional[str]
        # Ip pool allocated to Interconnect Gateway for Loopback Interfaces
        loopback_cidr: Optional[str]
        mrf_settings: Optional[InterconnectMrfSettings]
        resource_state: Optional[str]
        resource_state_message: Optional[str]
        resource_state_update_ts: Optional[str]
        service_chain_attachments: Optional[str]
        settings: Optional[InterconnectGatewaySettings]


    class ProcessResponse:
        # Procees Id of the task
        id: Optional[str]


