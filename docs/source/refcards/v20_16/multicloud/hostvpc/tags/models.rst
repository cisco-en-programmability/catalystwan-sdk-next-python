======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class HostVpcTagResponse:
        account_id: str
        cloud_type: str
        # Used for AWS, AWS GovCloud and GCP cloud types
        host_vpc_id: str
        region: str
        # Used for Azure and Azure GovCloud cloud types
        vnet_id: str
        account_name: Optional[str]
        # Used for AWS, AWS GovCloud and GCP cloud types
        host_vpc_name: Optional[str]
        # Used for Azure and Azure GovCloud cloud types
        resource_groups: Optional[str]
        tag: Optional[str]
        # Used for Azure and Azure GovCloud cloud types
        vnet_key: Optional[str]
        # Used for Azure and Azure GovCloud cloud types
        vpc_name: Optional[str]


    class Taskid:
        """
        Task id for polling status
        """

        id: Optional[str]


    class AllOfhostVpcTagPutHostVpcsItems:
        """
        Used for AWS, AWS GovCloud and GCP cloud types
        """

        account_id: str
        cloud_type: str
        # Used for AWS, AWS GovCloud and GCP cloud types
        host_vpc_id: str
        region: str
        # Used for Azure and Azure GovCloud cloud types
        vnet_id: str
        account_name: Optional[str]
        cgw_attachment: Optional[str]
        cgw_auto_attachment_flag: Optional[bool]
        # Used for AWS, AWS GovCloud and GCP cloud types
        host_vpc_name: Optional[str]
        id: Optional[str]
        interconnect_tag: Optional[str]
        label: Optional[str]
        # Used for Azure and Azure GovCloud cloud types
        resource_groups: Optional[str]
        tag: Optional[str]
        # Used for Azure and Azure GovCloud cloud types
        vnet_key: Optional[str]
        # Used for Azure and Azure GovCloud cloud types
        vpc_name: Optional[str]


    class AllOfhostVpcTagPutVnetsItems:
        """
        Used for Azure and Azure GovCloud cloud types
        """

        account_id: str
        cloud_type: str
        # Used for AWS, AWS GovCloud and GCP cloud types
        host_vpc_id: str
        region: str
        # Used for Azure and Azure GovCloud cloud types
        vnet_id: str
        account_name: Optional[str]
        cgw_attachment: Optional[str]
        cgw_auto_attachment_flag: Optional[bool]
        # Used for AWS, AWS GovCloud and GCP cloud types
        host_vpc_name: Optional[str]
        id: Optional[str]
        interconnect_tag: Optional[str]
        label: Optional[str]
        # Used for Azure and Azure GovCloud cloud types
        resource_groups: Optional[str]
        tag: Optional[str]
        # Used for Azure and Azure GovCloud cloud types
        vnet_key: Optional[str]
        # Used for Azure and Azure GovCloud cloud types
        vpc_name: Optional[str]


    class HostVpcTagPut:
        # Used for AWS, AWS GovCloud and GCP cloud types
        host_vpcs: Optional[List[AllOfhostVpcTagPutHostVpcsItems]]
        interconnect_tag: Optional[bool]
        tag_name: Optional[str]
        # Used for Azure and Azure GovCloud cloud types
        vnets: Optional[List[AllOfhostVpcTagPutVnetsItems]]


    class AllOfhostVpcTagPostHostVpcsItems:
        """
        Used for AWS, AWS GovCloud and GCP cloud types
        """

        account_id: str
        cloud_type: str
        # Used for AWS, AWS GovCloud and GCP cloud types
        host_vpc_id: str
        region: str
        # Used for Azure and Azure GovCloud cloud types
        vnet_id: str
        account_name: Optional[str]
        # Used for AWS, AWS GovCloud and GCP cloud types
        host_vpc_name: Optional[str]
        id: Optional[str]
        label: Optional[str]
        # Used for Azure and Azure GovCloud cloud types
        resource_groups: Optional[str]
        # Used for Azure and Azure GovCloud cloud types
        vnet_key: Optional[str]
        # Used for Azure and Azure GovCloud cloud types
        vpc_name: Optional[str]


    class AllOfhostVpcTagPostVnetsItems:
        """
        Used for Azure and Azure GovCloud cloud types
        """

        account_id: str
        cloud_type: str
        # Used for AWS, AWS GovCloud and GCP cloud types
        host_vpc_id: str
        region: str
        # Used for Azure and Azure GovCloud cloud types
        vnet_id: str
        account_name: Optional[str]
        cgw_attachment: Optional[str]
        cgw_auto_attachment_flag: Optional[bool]
        # Used for AWS, AWS GovCloud and GCP cloud types
        host_vpc_name: Optional[str]
        id: Optional[str]
        label: Optional[str]
        # Used for Azure and Azure GovCloud cloud types
        resource_groups: Optional[str]
        # Used for Azure and Azure GovCloud cloud types
        vnet_key: Optional[str]
        # Used for Azure and Azure GovCloud cloud types
        vpc_name: Optional[str]


    class HostVpcTagPost:
        # Used for AWS, AWS GovCloud and GCP cloud types
        host_vpcs: Optional[List[AllOfhostVpcTagPostHostVpcsItems]]
        interconnect_tag: Optional[bool]
        tag_name: Optional[str]
        # Used for Azure and Azure GovCloud cloud types
        vnets: Optional[List[AllOfhostVpcTagPostVnetsItems]]


