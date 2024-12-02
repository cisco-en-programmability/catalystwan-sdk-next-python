# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Literal, Optional
from dataclasses import dataclass, field as _field

CloudTypeParam = Literal["AWS", "AWS_GOVCLOUD", "AZURE", "AZURE_GOVCLOUD", "GCP"]


@dataclass
class InstanceSizeResponse:
    size: Optional[str] = _field(default=None)
    spec: Optional[str] = _field(default=None)
