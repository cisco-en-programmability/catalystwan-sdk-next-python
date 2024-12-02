# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional, List
from dataclasses import dataclass, field as _field


@dataclass
class FindVEdgeSoftwareVersionData:
    version: Optional[str] = _field(default=None)
    version_id: Optional[str] = _field(default=None, metadata={"alias": "versionId"})


@dataclass
class FindVEdgeSoftwareVersion:
    data: Optional[List[FindVEdgeSoftwareVersionData]] = _field(default=None)
