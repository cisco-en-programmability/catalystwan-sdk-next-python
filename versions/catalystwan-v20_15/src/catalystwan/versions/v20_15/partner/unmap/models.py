# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional, List
from dataclasses import dataclass, field as _field


@dataclass
class StatusResponse:
    status: Optional[str] = _field(default=None)


@dataclass
class MapDevicesRequest:
    devices: List[str]
