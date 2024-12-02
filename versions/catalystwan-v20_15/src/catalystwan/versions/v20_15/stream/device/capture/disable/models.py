# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class DisablePacketCaptureRes:
    status: Optional[str] = _field(default=None)
