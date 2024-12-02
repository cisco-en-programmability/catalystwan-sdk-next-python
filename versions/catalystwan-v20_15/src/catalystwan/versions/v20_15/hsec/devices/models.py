# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class GetHsecDevicesPayloadInner:
    configured_system_ip: Optional[str] = _field(
        default=None, metadata={"alias": "configuredSystemIP"}
    )
    device_model: Optional[str] = _field(
        default=None, metadata={"alias": "deviceModel"}
    )
    host_name: Optional[str] = _field(default=None, metadata={"alias": "hostName"})
    hsec_license_status: Optional[str] = _field(
        default=None, metadata={"alias": "hsecLicenseStatus"}
    )
    is_hsec_supported: Optional[bool] = _field(
        default=None, metadata={"alias": "isHsecSupported"}
    )
    reachability: Optional[str] = _field(default=None)
    tag: Optional[str] = _field(default=None)
    uuid: Optional[str] = _field(default=None)
