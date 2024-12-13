======
Models
======


.. code:: python

    from typing import List, Dict, Union, Literal, Optional, Any

    CloudTypeParam = Literal[
        "AWS", "AWS_GOVCLOUD", "AZURE", "AZURE_GOVCLOUD", "GCP"
    ]


    class MapSummaryAccountId:
        site_to_cloud_ncc_hub_name: Optional[str]
        site_to_cloud_ncc_spoke_name: Optional[str]
        site_to_cloud_primary_gcr_name: Optional[str]
        site_to_cloud_vpc_id: Optional[str]
        site_to_cloud_vpc_name: Optional[str]
        site_to_site_ncc_hub_name: Optional[str]
        site_to_site_vpc_id: Optional[str]
        site_to_site_vpc_name: Optional[str]
        wan_vpc_id: Optional[str]
        wan_vpc_name: Optional[str]


    class MapSummaryDevices:
        reachability: Optional[str]
        system_ip: Optional[str]
        uuid: Optional[str]


    class MapSummaryHostVpcs:
        account_id: Optional[str]
        host_vpc_id: Optional[str]
        tag: Optional[str]


    class MapSummaryTags:
        tag: Optional[str]


    class MapSummaryTunnels:
        accepted_route_count: Optional[int]
        last_status_change_timestamp: Optional[str]
        outer_ip_addr: Optional[str]
        status: Optional[str]
        status_message: Optional[str]
        tunnel_id: Optional[str]


    class MapSummaryVpns:
        vpn_id: Optional[str]


    class MapSummary:
        account_id: Optional[MapSummaryAccountId]
        account_name: Optional[str]
        additional_details: Optional[str]
        azure_virtual_wan_hub_id: Optional[str]
        cloud_gateway_name: Optional[str]
        cloud_gateway_solution: Optional[str]
        cloud_provider_mgmt_reference: Optional[str]
        cloud_type: Optional[str]
        connected_sites: Optional[int]
        connectivity_state: Optional[str]
        connectivity_state_update_ts: Optional[str]
        devices: Optional[List[MapSummaryDevices]]
        host_vpcs: Optional[MapSummaryHostVpcs]
        oper_state: Optional[str]
        region: Optional[str]
        status: Optional[str]
        tags: Optional[MapSummaryTags]
        tunnels: Optional[List[MapSummaryTunnels]]
        vpns: Optional[MapSummaryVpns]


