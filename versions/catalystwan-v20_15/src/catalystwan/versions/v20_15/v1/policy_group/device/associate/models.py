# Copyright 2024 Cisco Systems, Inc. and its affiliates
from dataclasses import dataclass
from dataclasses import field as _field
from typing import Any, List, Optional


@dataclass
class DeviceIdDef:
    id: str


@dataclass
class Default:
    """
    Policy Group Associate Post Request schema
    """

    # list of device ids that policy group need to be associated with
    devices: List[DeviceIdDef]
    # This is the documentation for associate POST API request schema for policy group.
    documentation: Optional[Any] = _field(default=None)
