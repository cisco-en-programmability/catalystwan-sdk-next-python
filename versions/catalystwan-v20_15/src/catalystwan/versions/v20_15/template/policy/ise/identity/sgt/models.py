# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional, List
from dataclasses import dataclass, field as _field


@dataclass
class SecurityGroup:
    description: Optional[str] = _field(default=None)
    id: Optional[str] = _field(default=None)
    name: Optional[str] = _field(default=None)
    tag: Optional[int] = _field(default=None)


@dataclass
class SgtResponse:
    """
    Security Groups Returned from ISE
    """

    security_groups: Optional[List[SecurityGroup]] = _field(
        default=None, metadata={"alias": "securityGroups"}
    )
