# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional, List
from dataclasses import dataclass, field as _field


@dataclass
class InterconnectSshKeyInfo:
    # Ssh Key Name
    key_name: Optional[str] = _field(default=None, metadata={"alias": "keyName"})
    # Ssh key Type
    key_type: Optional[str] = _field(default=None, metadata={"alias": "keyType"})
    # Ssh Key Value
    key_value: Optional[str] = _field(default=None, metadata={"alias": "keyValue"})


@dataclass
class InlineResponse20016:
    ssh_keys: Optional[List[InterconnectSshKeyInfo]] = _field(
        default=None, metadata={"alias": "sshKeys"}
    )
