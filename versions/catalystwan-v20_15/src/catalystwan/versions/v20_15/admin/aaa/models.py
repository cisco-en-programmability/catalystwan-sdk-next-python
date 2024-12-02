# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Literal, Optional, List
from dataclasses import dataclass, field as _field

AuthOrder = Literal["local", "radius", "tacacs"]


@dataclass
class Aaa:
    accounting: Optional[bool] = _field(default=None)
    admin_auth_order: Optional[bool] = _field(
        default=None, metadata={"alias": "adminAuthOrder"}
    )
    audit_disable: Optional[bool] = _field(
        default=None, metadata={"alias": "auditDisable"}
    )
    auth_fallback: Optional[bool] = _field(
        default=None, metadata={"alias": "authFallback"}
    )
    auth_order: Optional[List[AuthOrder]] = _field(
        default=None, metadata={"alias": "authOrder"}
    )
