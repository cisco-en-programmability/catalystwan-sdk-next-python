# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class SimpleKeyValueMapping:
    key: Optional[str] = _field(default=None)
    value: Optional[str] = _field(default=None)
