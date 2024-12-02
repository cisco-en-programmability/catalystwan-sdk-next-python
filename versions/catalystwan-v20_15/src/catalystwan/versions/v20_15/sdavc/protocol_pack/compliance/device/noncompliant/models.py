# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional, List
from dataclasses import dataclass, field as _field


@dataclass
class CompliantDeviceRequest:
    devices: Optional[List[str]] = _field(default=None)
    protocol_pack_name: Optional[str] = _field(
        default=None, metadata={"alias": "protocolPackName"}
    )
