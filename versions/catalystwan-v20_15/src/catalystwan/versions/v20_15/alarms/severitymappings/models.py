# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional, List
from dataclasses import dataclass, field as _field


@dataclass
class SimpleKeyValueMapping:
    key: Optional[str] = _field(default=None)
    value: Optional[str] = _field(default=None)


@dataclass
class AlarmSeverityMapping:
    associated_alarms: Optional[List[SimpleKeyValueMapping]] = _field(
        default=None, metadata={"alias": "associatedAlarms"}
    )
    key: Optional[str] = _field(default=None)
    value: Optional[str] = _field(default=None)
