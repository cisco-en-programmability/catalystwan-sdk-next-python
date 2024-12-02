# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Literal
from dataclasses import dataclass, field as _field

InterconnectTypeParam = Literal["EQUINIX", "MEGAPORT"]


@dataclass
class GatewaysConfiggroupBody:
    config_group_name: str = _field(metadata={"alias": "configGroupName"})
