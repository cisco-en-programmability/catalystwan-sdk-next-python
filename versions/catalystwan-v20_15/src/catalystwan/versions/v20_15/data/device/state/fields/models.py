# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class GenerateDeviceStateDataFieldsInner:
    data_type: Optional[str] = _field(default=None, metadata={"alias": "dataType"})
    display: Optional[str] = _field(default=None)
    property: Optional[str] = _field(default=None)
