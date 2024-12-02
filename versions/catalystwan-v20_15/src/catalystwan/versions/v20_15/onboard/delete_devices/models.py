# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional, List
from dataclasses import dataclass, field as _field


@dataclass
class DeleteResponseInner:
    host: Optional[str] = _field(default=None)
    reason: Optional[str] = _field(default=None)


@dataclass
class DeleteDetails:
    devices: Optional[List[str]] = _field(default=None)
