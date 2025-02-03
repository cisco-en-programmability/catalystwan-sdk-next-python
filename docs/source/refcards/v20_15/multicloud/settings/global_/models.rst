======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    CloudTypeParam = Literal[
        "AWS", "AWS_GOVCLOUD", "AZURE", "AZURE_GOVCLOUD", "GCP"
    ]


    class MulticloudSystemSettings:
        enable_monitoring: Optional[bool]
        # Enable or disable Configuration Group for Gateways
        use_configuration_group: Optional[str]


    class GlobalSettings:
        # Used for GCP, AWS and AWS GovCloud Global settings
        cgw_bgp_asn_offset: str
        cloud_gateway_solution: str
        cloud_type: str
        # Used for GCP, AWS and AWS GovCloud Global settings
        instance_size: str
        ip_subnet_pool: str
        # Used for GCP, Azure and Azure GovCloud Global settings
        org_bgp_asn: str
        # Used for Azure/Azure GovCloud Global settings
        sku_scale_unit: str
        software_image_id: str
        # Used for AWS/AWS GovCloud Global settings
        account_id: Optional[str]
        enable_auto_correct: Optional[str]
        # Used for Azure Global settings
        enable_def_route_advertize: Optional[str]
        # Used for Azure Global settings
        enable_monitoring: Optional[str]
        enable_periodic_audit: Optional[str]
        intra_tag_comm: Optional[str]
        # Used for GCP, AWS and AWS GovCloud Global settings
        map_tvpc: Optional[str]
        multicloud_system_settings: Optional[MulticloudSystemSettings]
        name: Optional[str]
        # Used for GCP Global settings
        network_tier: Optional[str]
        # Used for GCP Global settings
        policy_management: Optional[str]
        # Used for AWS/AWS GovCloud Global settings
        program_default_route: Optional[str]
        # Used for AWS/AWS GovCloud Global settings
        region: Optional[str]
        # Used for GCP Global settings
        service_dir_poll_timer: Optional[str]
        # Used for AWS/AWS GovCloud Global settings
        tunnel_count: Optional[str]
        # Used for GCP, AWS and AWS GovCloud Global settings
        tunnel_type: Optional[str]


    class Taskid:
        """
        Task id for polling status
        """

        id: Optional[str]


