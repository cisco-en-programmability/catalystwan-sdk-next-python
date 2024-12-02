# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class DeviceBlistDeleteResponsePayload:
    """
    Device blist delete response schema
    """

    action: Optional[str] = _field(default=None)
    message: Optional[str] = _field(default=None)
