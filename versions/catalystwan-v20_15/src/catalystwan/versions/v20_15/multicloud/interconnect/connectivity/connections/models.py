# Copyright 2024 Cisco Systems, Inc. and its affiliates
from dataclasses import dataclass
from dataclasses import field as _field
from typing import Optional


@dataclass
class ProcessResponse:
    # Procees Id of the task
    id: Optional[str] = _field(default=None)
