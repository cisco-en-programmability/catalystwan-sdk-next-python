# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class HostVpcsResponse:
    account_id: str = _field(metadata={"alias": "accountId"})
    cloud_type: str = _field(metadata={"alias": "cloudType"})
    # Used for AWS, AWS GovCloud and GCP cloud types
    host_vpc_id: str = _field(metadata={"alias": "hostVpcId"})
    region: str
    # Used for Azure and Azure GovCloud cloud types
    vnet_id: str = _field(metadata={"alias": "vnetId"})
    account_name: Optional[str] = _field(
        default=None, metadata={"alias": "accountName"}
    )
    # Used for AWS, AWS GovCloud and GCP cloud types
    host_vpc_name: Optional[str] = _field(
        default=None, metadata={"alias": "hostVpcName"}
    )
    # Used for Azure and Azure GovCloud cloud types
    resource_groups: Optional[str] = _field(
        default=None, metadata={"alias": "resourceGroups"}
    )
    # Used for Azure and Azure GovCloud cloud types
    vnet_key: Optional[str] = _field(default=None, metadata={"alias": "vnetKey"})
    # Used for Azure and Azure GovCloud cloud types
    vpc_name: Optional[str] = _field(default=None, metadata={"alias": "vpcName"})
