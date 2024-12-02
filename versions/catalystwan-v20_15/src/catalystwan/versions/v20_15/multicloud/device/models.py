# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class WanEdgeDevicesResponse:
    configured_host_name: Optional[str] = _field(
        default=None, metadata={"alias": "configuredHostName"}
    )
    configured_system_ip: Optional[str] = _field(
        default=None, metadata={"alias": "configuredSystemIp"}
    )
    device_model: Optional[str] = _field(
        default=None, metadata={"alias": "deviceModel"}
    )
    is_payg_uuid: Optional[bool] = _field(
        default=None, metadata={"alias": "isPaygUuid"}
    )
    uuid: Optional[str] = _field(default=None)
