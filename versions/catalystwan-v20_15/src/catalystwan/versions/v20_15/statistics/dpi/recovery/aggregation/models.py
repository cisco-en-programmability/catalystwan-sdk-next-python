# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional, List
from dataclasses import dataclass, field as _field


@dataclass
class FecAndPktDupResponseHeader:
    columns: Optional[List[str]] = _field(default=None)
    fields: Optional[List[str]] = _field(default=None)
    generated_on: Optional[int] = _field(
        default=None, metadata={"alias": "generatedOn"}
    )


@dataclass
class FecAndPktDupResponse:
    data: Optional[List[str]] = _field(default=None)
    header: Optional[FecAndPktDupResponseHeader] = _field(default=None)
