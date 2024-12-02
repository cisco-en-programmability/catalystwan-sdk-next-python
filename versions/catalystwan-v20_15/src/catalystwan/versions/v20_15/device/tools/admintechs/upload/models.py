# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class AdminTechsUploadReq:
    request_token_id: Optional[str] = _field(
        default=None, metadata={"alias": "requestTokenId"}
    )
    sr_number: Optional[str] = _field(default=None)
    token: Optional[str] = _field(default=None)
    vpn: Optional[str] = _field(default=None)
