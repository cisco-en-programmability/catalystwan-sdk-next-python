# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional
from dataclasses import dataclass, field as _field


@dataclass
class LinkObject:
    href: Optional[str] = _field(default=None)
    rel: Optional[str] = _field(default=None)
    type_: Optional[str] = _field(default=None, metadata={"alias": "type"})


@dataclass
class VersionInformation:
    current_server_version: Optional[str] = _field(
        default=None, metadata={"alias": "currentServerVersion"}
    )
    link: Optional[LinkObject] = _field(default=None)
    supported_versions: Optional[str] = _field(
        default=None, metadata={"alias": "supportedVersions"}
    )


@dataclass
class ConnectResponse:
    """
    Response from ISE ERS version info api
    """

    version_info: Optional[VersionInformation] = _field(
        default=None, metadata={"alias": "VersionInfo"}
    )
