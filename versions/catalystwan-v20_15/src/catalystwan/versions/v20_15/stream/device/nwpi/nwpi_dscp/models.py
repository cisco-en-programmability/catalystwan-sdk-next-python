# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class NwpiDscpResponsePayloadInner:
    """
    DSCP for GET response
    """

    dscp_name: Optional[str] = _field(default=None, metadata={"alias": "dscpName"})
    value: Optional[int] = _field(default=None)
