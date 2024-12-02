# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class CreateResponse:
    """
    Response from PxGrid node creation on ISE
    """

    node_name: Optional[str] = _field(default=None, metadata={"alias": "nodeName"})
    password: Optional[str] = _field(default=None)
    user_name: Optional[str] = _field(default=None, metadata={"alias": "userName"})


@dataclass
class CreateBody:
    """
    Body for PxGrid node create on ISE
    """

    node_name: Optional[str] = _field(default=None, metadata={"alias": "nodeName"})
