# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class AppRouteAggResp:
    count: Optional[int] = _field(default=None)
    entry_time: Optional[str] = _field(default=None)
    local_color: Optional[str] = _field(default=None)
    loss_percentage: Optional[int] = _field(default=None)
