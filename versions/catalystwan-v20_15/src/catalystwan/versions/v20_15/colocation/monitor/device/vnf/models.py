# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class DeviceUuid:
    """
    This is valid DeviceUuid
    """

    device_uuid: Optional[str] = _field(default=None, metadata={"alias": "deviceUuid"})
