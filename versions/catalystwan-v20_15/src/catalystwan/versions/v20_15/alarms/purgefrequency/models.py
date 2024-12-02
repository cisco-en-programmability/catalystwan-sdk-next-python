# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class PurgeFrequency:
    active_time: Optional[str] = _field(default=None, metadata={"alias": "activeTime"})
    interval: Optional[str] = _field(default=None)
