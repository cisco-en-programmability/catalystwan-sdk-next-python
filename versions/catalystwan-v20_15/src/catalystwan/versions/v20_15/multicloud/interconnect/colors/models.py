# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Literal, Optional, List
from dataclasses import dataclass, field as _field

TunnelTypeParam = Literal["loopbackCgw", "loopbackTransit"]


@dataclass
class InlineResponse2002:
    loopback_cgw_color: Optional[List[str]] = _field(
        default=None, metadata={"alias": "loopbackCgwColor"}
    )
    loopback_tunnel_color: Optional[List[str]] = _field(
        default=None, metadata={"alias": "loopbackTunnelColor"}
    )
