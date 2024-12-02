# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class EntityOwnershipInfo:
    bucket: Optional[str] = _field(default=None)
    entity_name: Optional[str] = _field(default=None, metadata={"alias": "entityName"})
    owner: Optional[str] = _field(default=None)
