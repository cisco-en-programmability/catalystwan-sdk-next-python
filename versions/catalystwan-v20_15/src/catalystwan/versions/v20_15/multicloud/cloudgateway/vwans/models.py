# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class VwanListResponse:
    source: Optional[str] = _field(default=None)
    vwan_id: Optional[str] = _field(default=None, metadata={"alias": "vwanId"})
    vwan_name: Optional[str] = _field(default=None, metadata={"alias": "vwanName"})
