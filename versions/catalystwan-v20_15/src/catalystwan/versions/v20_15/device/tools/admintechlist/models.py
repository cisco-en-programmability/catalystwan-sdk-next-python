# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class AdminTechListRes:
    creation_time: Optional[int] = _field(
        default=None, metadata={"alias": "creationTime"}
    )
    file_name: Optional[str] = _field(default=None, metadata={"alias": "fileName"})
    request_token_id: Optional[str] = _field(
        default=None, metadata={"alias": "requestTokenId"}
    )
    size: Optional[int] = _field(default=None)
    state: Optional[str] = _field(default=None)


@dataclass
class AdminTechListReq:
    device_ip: Optional[str] = _field(default=None, metadata={"alias": "deviceIP"})
