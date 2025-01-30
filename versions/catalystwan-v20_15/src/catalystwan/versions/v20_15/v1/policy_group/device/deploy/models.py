# Copyright 2024 Cisco Systems, Inc. and its affiliates
from dataclasses import dataclass
from dataclasses import field as _field
from typing import Any, List, Optional


@dataclass
class DeviceIdDef:
    id: str


@dataclass
class DeployPolicyGroupPostRequest:
    """
    Policy Group Deploy Request schema
    """

    # list of device ids that policy group need to be deployed
    devices: Optional[List[DeviceIdDef]] = _field(default=None)
    # This is the documentation for DEPLOY API request schema for policy group.
    documentation: Optional[Any] = _field(default=None)
