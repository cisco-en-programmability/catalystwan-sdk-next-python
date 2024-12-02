# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class SetLifeCycle:
    device_life_cycle_needed: Optional[bool] = _field(
        default=None, metadata={"alias": "DeviceLifeCycleNeeded"}
    )
