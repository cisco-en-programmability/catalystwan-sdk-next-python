# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class EnrollOtpResponse:
    """
    Enroll CDNA Server Response.
    """

    auth_token: Optional[str] = _field(default=None, metadata={"alias": "authToken"})
    cdna_server_ip: Optional[str] = _field(
        default=None, metadata={"alias": "cdnaServerIP"}
    )
    cline_id: Optional[str] = _field(default=None)
    enrolled: Optional[bool] = _field(default=None)
    last_updated: Optional[str] = _field(
        default=None, metadata={"alias": "lastUpdated"}
    )
    member_id: Optional[str] = _field(default=None)
    token_url: Optional[str] = _field(default=None)


@dataclass
class EnrollOtpSettings:
    token: str
