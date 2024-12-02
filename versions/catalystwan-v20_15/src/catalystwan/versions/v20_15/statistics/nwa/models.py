# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Literal, Optional
from dataclasses import dataclass, field as _field

Health = Literal["fair", "good", "poor"]


@dataclass
class NetworkAvailabilityResp:
    health: Health
    jitter: int
    latency: int
    loss: int
    availability: Optional[int] = _field(default=None)
    latitude: Optional[str] = _field(default=None)
    longitude: Optional[str] = _field(default=None)
    siteid: Optional[str] = _field(default=None)
    sitename: Optional[str] = _field(default=None)
