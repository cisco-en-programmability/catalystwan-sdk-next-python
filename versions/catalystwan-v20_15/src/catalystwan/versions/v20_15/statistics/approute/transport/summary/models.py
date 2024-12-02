# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class AppRouteFecAggRespInner:
    count: Optional[int] = _field(default=None)
    entry_time: Optional[str] = _field(default=None)
    fec_loss_recovery: Optional[str] = _field(
        default=None, metadata={"alias": "fecLossRecovery"}
    )
    loss_percentage: Optional[int] = _field(default=None)
    name: Optional[str] = _field(default=None)
    proto: Optional[str] = _field(default=None)
    state: Optional[str] = _field(default=None)
