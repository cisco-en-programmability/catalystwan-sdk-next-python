# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class DisabledAlarmDetails:
    end_time: Optional[str] = _field(default=None, metadata={"alias": "endTime"})
    event_name: Optional[str] = _field(default=None, metadata={"alias": "eventName"})
    start_time: Optional[str] = _field(default=None, metadata={"alias": "startTime"})
