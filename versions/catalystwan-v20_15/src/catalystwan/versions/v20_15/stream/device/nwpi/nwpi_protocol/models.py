# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class NwpiProtocolResponsePayloadInner:
    """
    Protocol for GET response
    """

    protocol_name: Optional[str] = _field(
        default=None, metadata={"alias": "protocolName"}
    )
    value: Optional[int] = _field(default=None)
