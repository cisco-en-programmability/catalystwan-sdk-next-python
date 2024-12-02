# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class SyncDevicesResp:
    process_id: Optional[str] = _field(default=None, metadata={"alias": "processId"})


@dataclass
class SmartAccountModel:
    client_credentials: Optional[bool] = _field(
        default=None, metadata={"alias": "clientCredentials"}
    )
    env: Optional[str] = _field(default=None)
    organization_name: Optional[str] = _field(default=None)
    password: Optional[str] = _field(default=None)
    username: Optional[str] = _field(default=None)
    validity_string: Optional[str] = _field(default=None)
