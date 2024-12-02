# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional, List
from dataclasses import dataclass, field as _field


@dataclass
class InlineResponse2007:
    port_speeds: Optional[List[str]] = _field(
        default=None, metadata={"alias": "portSpeeds"}
    )
