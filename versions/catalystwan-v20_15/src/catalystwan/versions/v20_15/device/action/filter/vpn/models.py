# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional, List
from dataclasses import dataclass, field as _field


@dataclass
class CreateFilterVpnList:
    vedge: Optional[List[str]] = _field(default=None)
    vsmart: Optional[List[str]] = _field(default=None)
