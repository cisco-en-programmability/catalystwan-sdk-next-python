# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class Vpnid:
    """
    This is the valid list of VPN-IDs
    """

    vpn: Optional[str] = _field(default=None)
