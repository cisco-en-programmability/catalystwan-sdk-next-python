# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class InterfaceAggResp:
    count: Optional[int] = _field(default=None)
    entry_time: Optional[str] = _field(default=None)
    interface: Optional[str] = _field(default=None)
    rx_kbps: Optional[int] = _field(default=None)
    tx_kbps: Optional[int] = _field(default=None)
    vdevice_name: Optional[str] = _field(default=None)
