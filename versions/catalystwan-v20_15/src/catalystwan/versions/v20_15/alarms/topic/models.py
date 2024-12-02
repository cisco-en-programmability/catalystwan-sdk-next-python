# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class AlarmTopic:
    device_ip: Optional[str] = _field(default=None, metadata={"alias": "device-ip"})
    server_ip: Optional[str] = _field(default=None, metadata={"alias": "server-ip"})
    topic: Optional[str] = _field(default=None)
