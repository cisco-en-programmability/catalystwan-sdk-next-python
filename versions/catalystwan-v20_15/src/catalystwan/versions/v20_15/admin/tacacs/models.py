# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Literal, Optional, List
from dataclasses import dataclass, field as _field

Authentication = Literal["ASCII", "PAP"]


@dataclass
class TacacsServer:
    address: Optional[str] = _field(default=None)
    auth_port: Optional[int] = _field(default=None, metadata={"alias": "authPort"})
    key: Optional[str] = _field(default=None)
    priority: Optional[int] = _field(default=None)
    secret_key: Optional[str] = _field(default=None, metadata={"alias": "secretKey"})
    vpn: Optional[int] = _field(default=None)
    vpn_ip_subnet: Optional[str] = _field(
        default=None, metadata={"alias": "vpnIpSubnet"}
    )


@dataclass
class Tacacs:
    authentication: Optional[Authentication] = _field(default=None)
    server: Optional[List[TacacsServer]] = _field(default=None)
    timeout: Optional[int] = _field(default=None)
