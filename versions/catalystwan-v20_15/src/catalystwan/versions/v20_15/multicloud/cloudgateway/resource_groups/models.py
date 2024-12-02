# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class ResourceGroupsResponse:
    resource_group_id: Optional[str] = _field(
        default=None, metadata={"alias": "resourceGroupId"}
    )
    source: Optional[str] = _field(default=None)
