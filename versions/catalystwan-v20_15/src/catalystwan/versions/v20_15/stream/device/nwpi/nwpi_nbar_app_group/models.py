# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional, List, Any
from dataclasses import dataclass, field as _field


@dataclass
class NwpiNbarAppGroupResponsePayloadInner:
    """
    Nbar Application Group for GET response
    """

    entries: Optional[List[Any]] = _field(default=None)
    name: Optional[str] = _field(default=None)
