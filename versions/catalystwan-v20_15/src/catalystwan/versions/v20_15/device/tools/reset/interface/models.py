# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class ResetInterfaceReq:
    ifname: Optional[str] = _field(default=None)
    vpn_id: Optional[str] = _field(default=None, metadata={"alias": "vpnId"})
