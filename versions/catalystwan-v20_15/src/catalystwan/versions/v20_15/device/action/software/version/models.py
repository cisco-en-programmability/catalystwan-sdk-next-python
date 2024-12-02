# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional, List
from dataclasses import dataclass, field as _field


@dataclass
class FindSoftwareVersionData:
    version: Optional[str] = _field(default=None)


@dataclass
class FindSoftwareVersion:
    data: Optional[List[FindSoftwareVersionData]] = _field(default=None)
