# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class MslaLicensesInner:
    available: Optional[str] = _field(default=None)
    billing_type: Optional[str] = _field(default=None)
    display_name: Optional[str] = _field(default=None)
    end_date: Optional[str] = _field(default=None)
    in_use: Optional[str] = _field(default=None, metadata={"alias": "inUse"})
    license_category: Optional[str] = _field(default=None)
    saname: Optional[str] = _field(default=None)
    subscription_id: Optional[str] = _field(default=None)
    tag: Optional[str] = _field(default=None)
    vaname: Optional[str] = _field(default=None)
