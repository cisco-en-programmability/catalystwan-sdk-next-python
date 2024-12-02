# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional, List
from dataclasses import dataclass, field as _field


@dataclass
class SdraDeviceStatsShort:
    host_name: Optional[str] = _field(default=None)
    ipsec_anyconnect: Optional[int] = _field(default=None)
    ipsec_soho: Optional[int] = _field(default=None)
    ipsec_unknown: Optional[int] = _field(default=None)
    site_id: Optional[int] = _field(default=None)
    sslvpn_anyconnect: Optional[int] = _field(default=None)
    system_ip: Optional[str] = _field(default=None)


@dataclass
class SdraSessionCount:
    ipsec_anyconnect: Optional[int] = _field(default=None)
    ipsec_soho: Optional[int] = _field(default=None)
    ipsec_unknown: Optional[int] = _field(default=None)
    sslvpn_anyconnect: Optional[int] = _field(default=None)


@dataclass
class SdraSessionSummary:
    top: Optional[List[SdraDeviceStatsShort]] = _field(default=None)
    total: Optional[SdraSessionCount] = _field(default=None)
