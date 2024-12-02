# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class DeviceLists:
    entry_time: int
    device_ip: Optional[str] = _field(default=None)
    host_name: Optional[str] = _field(default=None)
    site_name: Optional[str] = _field(default=None)
