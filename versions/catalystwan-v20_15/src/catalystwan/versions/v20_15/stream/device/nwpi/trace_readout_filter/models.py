# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional, List
from dataclasses import dataclass, field as _field


@dataclass
class EventReadoutFilterResponsePayload:
    """
    Event readouts Filter Response schema
    """

    # User Name List
    user_name: Optional[List[str]] = _field(
        default=None, metadata={"alias": "userName"}
    )
