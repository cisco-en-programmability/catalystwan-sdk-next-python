# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Literal, Optional
from dataclasses import dataclass, field as _field

SeverityLevel = Literal["CRITICAL", "MAJOR", "MEDIUM", "MINOR"]


@dataclass
class EventsBySeverity:
    component: Optional[str] = _field(default=None)
    details: Optional[str] = _field(default=None)
    entry_time: Optional[str] = _field(default=None)
    eventname: Optional[str] = _field(default=None)
    host_name: Optional[str] = _field(default=None)
    severity_level: Optional[SeverityLevel] = _field(default=None)
    system_ip: Optional[str] = _field(default=None)
