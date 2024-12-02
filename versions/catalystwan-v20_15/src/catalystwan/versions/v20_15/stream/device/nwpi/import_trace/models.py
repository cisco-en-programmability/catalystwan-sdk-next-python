# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class ImportTraceResponse:
    msg: Optional[str] = _field(default=None)
    state: Optional[bool] = _field(default=None)


@dataclass
class ImportTraceRequest:
    file: Optional[str] = _field(default=None)
