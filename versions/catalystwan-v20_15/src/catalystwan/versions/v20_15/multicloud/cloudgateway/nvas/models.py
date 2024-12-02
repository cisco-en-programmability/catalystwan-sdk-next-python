# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional, List
from dataclasses import dataclass, field as _field


@dataclass
class NvasResponse:
    nva_id: Optional[str] = _field(default=None, metadata={"alias": "nvaId"})
    nva_name: Optional[str] = _field(default=None, metadata={"alias": "nvaName"})
    source: Optional[str] = _field(default=None)
    uuids: Optional[List[str]] = _field(default=None)
