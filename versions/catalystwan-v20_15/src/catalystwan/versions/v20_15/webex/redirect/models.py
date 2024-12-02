# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class RedirectCodeResponse:
    message: Optional[str] = _field(default=None)
    type_: Optional[str] = _field(default=None, metadata={"alias": "type"})
