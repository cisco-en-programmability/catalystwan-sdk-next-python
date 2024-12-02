# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Literal, Optional
from dataclasses import dataclass, field as _field

HealthParam = Literal["FAIR", "GOOD", "POOR"]


@dataclass
class ApplicationSiteItem:
    health: str
    jitter: int
    latency: int
    loss: int
    path: str
    qoe: Optional[int] = _field(default=None)
