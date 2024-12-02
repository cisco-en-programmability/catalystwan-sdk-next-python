# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class NwpiResponsePayload:
    """
    Nwpi common response payload schema
    """

    status: Optional[str] = _field(default=None)
