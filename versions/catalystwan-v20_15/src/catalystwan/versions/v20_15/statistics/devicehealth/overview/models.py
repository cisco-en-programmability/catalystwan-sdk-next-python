# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Literal, Optional, List
from dataclasses import dataclass, field as _field

Health = Literal["fair", "good", "n/a", "poor"]

PersonalityParam = Literal["vbond", "vedge", "vmanage", "vsmart"]


@dataclass
class DeviceHealthDetailItem:
    cpu_load: int
    health: Health
    health_score: int
    host_name: str
    memory_utilization: int
    qoe: int
    reachability: str
    site_id: str
    system_ip: str


@dataclass
class DeviceHealthOverviewDetail:
    fair: Optional[List[DeviceHealthDetailItem]] = _field(default=None)
    good: Optional[List[DeviceHealthDetailItem]] = _field(default=None)
    poor: Optional[List[DeviceHealthDetailItem]] = _field(default=None)


@dataclass
class DeviceHealthOverviewTotal:
    fair: Optional[int] = _field(default=None)
    good: Optional[int] = _field(default=None)
    poor: Optional[int] = _field(default=None)


@dataclass
class DeviceHealthOverview:
    detail: Optional[DeviceHealthOverviewDetail] = _field(default=None)
    total: Optional[DeviceHealthOverviewTotal] = _field(default=None)
