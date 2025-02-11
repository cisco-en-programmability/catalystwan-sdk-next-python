======
Models
======


.. code:: python

    from typing import Union, Dict, Optional, Literal, List, Any

    CloudTypeParam = Literal["AWS", "AZURE", "GCP"]


    class AzureVirtualWanTagList:
        """
        Azure Virtual WAN Tag Object
        """

        name: Optional[str]
        value: Optional[str]


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


    class InlineResponse2009VWans:
        # Azure Virtual Wan
        v_wan: Optional[AzureVirtualWan]
        v_wan_in_use: Optional[bool]


    class InlineResponse2009:
        v_wans: Optional[List[InlineResponse2009VWans]]


