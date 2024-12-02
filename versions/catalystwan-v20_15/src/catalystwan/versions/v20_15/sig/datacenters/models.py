# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional, List
from dataclasses import dataclass, field as _field


@dataclass
class MappingEntries:
    city_country: Optional[str] = _field(
        default=None, metadata={"alias": "CITY/COUNTRY"}
    )
    fqdn: Optional[str] = _field(default=None, metadata={"alias": "FQDN"})
    ip: Optional[str] = _field(default=None, metadata={"alias": "IP"})


@dataclass
class GetDataCenters:
    mapping: Optional[List[MappingEntries]] = _field(default=None)
    title: Optional[str] = _field(default=None)
