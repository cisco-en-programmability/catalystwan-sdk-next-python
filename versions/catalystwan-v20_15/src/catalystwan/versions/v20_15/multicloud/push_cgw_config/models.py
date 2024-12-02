# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class Taskid:
    """
    Task id for polling status
    """

    id: Optional[str] = _field(default=None)


@dataclass
class PushCgwConfig:
    cloud_gateway_name: str = _field(metadata={"alias": "cloudGatewayName"})
    cloud_type: str = _field(metadata={"alias": "cloudType"})
