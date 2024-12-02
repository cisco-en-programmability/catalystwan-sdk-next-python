# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional, Any
from dataclasses import dataclass, field as _field


@dataclass
class AppQosStateResponsePayloadInner:
    """
    QoS Application state schema for GET response
    """

    data: Optional[Any] = _field(default=None)
    entry_time: Optional[int] = _field(default=None)
    tenant: Optional[str] = _field(default=None)
    trace_id: Optional[int] = _field(default=None, metadata={"alias": "trace-id"})
    type_: Optional[str] = _field(default=None, metadata={"alias": "type"})
