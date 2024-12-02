# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class GetTenantManagementSystemIPsInner:
    chasis_number: Optional[str] = _field(
        default=None, metadata={"alias": "chasisNumber"}
    )
    device_type: Optional[str] = _field(default=None, metadata={"alias": "deviceType"})
    management_system_ip: Optional[str] = _field(
        default=None, metadata={"alias": "managementSystemIP"}
    )
    serial_number: Optional[str] = _field(
        default=None, metadata={"alias": "serialNumber"}
    )
