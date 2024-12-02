# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class Tokens:
    """
    Response from Cisco SecureX token API
    """

    access_token: Optional[str] = _field(default=None)
    expires_in: Optional[int] = _field(default=None)
    refresh_token: Optional[str] = _field(default=None)
    scope: Optional[str] = _field(default=None)
    token_type: Optional[str] = _field(default=None)
