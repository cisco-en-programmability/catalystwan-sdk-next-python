# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class LicenseDistributionResult:
    display_name: Optional[str] = _field(default=None)
    last_updated: Optional[str] = _field(
        default=None, metadata={"alias": "lastUpdated"}
    )
    tag: Optional[str] = _field(default=None)
    total_devices: Optional[int] = _field(
        default=None, metadata={"alias": "totalDevices"}
    )
    total_license: Optional[int] = _field(
        default=None, metadata={"alias": "totalLicense"}
    )


@dataclass
class LicenseDistribution:
    result: Optional[LicenseDistributionResult] = _field(default=None)
