# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Literal, Optional, List
from dataclasses import dataclass, field as _field

CloudTypeParam = Literal["AWS", "AWS_GOVCLOUD", "AZURE", "AZURE_GOVCLOUD", "GCP"]


@dataclass
class GetTunnelsResponsePrivateIp:
    hostname: Optional[str] = _field(default=None)
    tunnels: Optional[str] = _field(default=None)


@dataclass
class GetTunnelsResponse:
    private_ip: Optional[List[GetTunnelsResponsePrivateIp]] = _field(
        default=None, metadata={"alias": "Private IP"}
    )
