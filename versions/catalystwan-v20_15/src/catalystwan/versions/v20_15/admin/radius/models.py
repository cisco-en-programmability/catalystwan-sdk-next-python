# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional, List
from dataclasses import dataclass, field as _field


@dataclass
class RadiusServer:
    host: str
    port: int
    secret: str


@dataclass
class Radius:
    retransmit: Optional[int] = _field(default=None)
    server: Optional[List[RadiusServer]] = _field(default=None)
    timeout: Optional[int] = _field(default=None)
