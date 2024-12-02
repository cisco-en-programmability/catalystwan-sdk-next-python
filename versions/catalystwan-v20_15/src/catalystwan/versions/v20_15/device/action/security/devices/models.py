# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Literal, Optional
from dataclasses import dataclass, field as _field

PolicyTypeParam = Literal[
    "advancedMalwareProtection",
    "dnsSecurity",
    "intrusionPrevention",
    "sslDecryption",
    "urlFiltering",
    "zoneBasedFW",
]


@dataclass
class GroupId:
    """
    This is the valid GroupId
    """

    group_id: Optional[str] = _field(default=None, metadata={"alias": "groupId"})
