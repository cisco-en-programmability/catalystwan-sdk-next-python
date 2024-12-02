# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional, List
from dataclasses import dataclass, field as _field


@dataclass
class PartnerSite:
    partner_id: Optional[str] = _field(default=None, metadata={"alias": "partnerId"})
    sites: Optional[List[str]] = _field(default=None)


@dataclass
class VpnListResHeader:
    generated_on: Optional[int] = _field(
        default=None, metadata={"alias": "generatedOn"}
    )


@dataclass
class SdaSitesRes:
    data: Optional[List[PartnerSite]] = _field(default=None)
    header: Optional[VpnListResHeader] = _field(default=None)
