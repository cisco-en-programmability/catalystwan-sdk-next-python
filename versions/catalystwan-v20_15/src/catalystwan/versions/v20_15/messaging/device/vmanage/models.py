# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional, List
from dataclasses import dataclass, field as _field


@dataclass
class MessagingResp:
    device_ip: Optional[str] = _field(default=None, metadata={"alias": "deviceIP"})
    vmanages: Optional[List[str]] = _field(default=None)
