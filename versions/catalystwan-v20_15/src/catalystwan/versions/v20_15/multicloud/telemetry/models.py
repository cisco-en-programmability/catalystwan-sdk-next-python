# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional, List
from dataclasses import dataclass, field as _field


@dataclass
class Taskid:
    """
    Task id for polling status
    """

    id: Optional[str] = _field(default=None)


@dataclass
class TelemetryRequests:
    cloud_type: str = _field(metadata={"alias": "cloudType"})
    cgw_list: Optional[List[str]] = _field(default=None, metadata={"alias": "cgwList"})
