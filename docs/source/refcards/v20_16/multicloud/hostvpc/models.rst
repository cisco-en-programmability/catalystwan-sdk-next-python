======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class HostVpcsResponse:
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
        # Used for Azure and Azure GovCloud cloud types
        vnet_key: Optional[str]
        # Used for Azure and Azure GovCloud cloud types
        vpc_name: Optional[str]


