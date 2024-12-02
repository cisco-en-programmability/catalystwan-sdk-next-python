# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class SdraHeadendSummary:
    ipsec_enabled: Optional[int] = _field(default=None)
    sslvpn_enabled: Optional[int] = _field(default=None)
