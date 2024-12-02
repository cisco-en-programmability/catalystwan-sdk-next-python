# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class Codes:
    """
    Response from Cisco SecureX device_authorization API
    """

    device_code: Optional[str] = _field(default=None)
    expires_in: Optional[int] = _field(default=None)
    interval: Optional[int] = _field(default=None)
    user_code: Optional[str] = _field(default=None)
    verification_uri: Optional[str] = _field(default=None)
    verification_uri_complete: Optional[str] = _field(default=None)
