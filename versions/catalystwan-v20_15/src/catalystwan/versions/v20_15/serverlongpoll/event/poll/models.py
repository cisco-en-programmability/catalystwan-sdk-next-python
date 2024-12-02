# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class EventName:
    """
    This is valid eventName
    """

    event_name: Optional[str] = _field(default=None, metadata={"alias": "eventName"})
