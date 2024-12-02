# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class VpnGatewayResponse:
    source: Optional[str] = _field(default=None)
    vpn_gateway_id: Optional[str] = _field(
        default=None, metadata={"alias": "vpnGatewayId"}
    )
    vpn_gateway_name: Optional[str] = _field(
        default=None, metadata={"alias": "vpnGatewayName"}
    )
