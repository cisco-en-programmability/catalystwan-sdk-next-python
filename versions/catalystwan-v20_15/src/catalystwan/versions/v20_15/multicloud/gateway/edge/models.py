# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Literal, Optional
from dataclasses import dataclass, field as _field

EdgeTypeParam = Literal["EQUINIX", "MEGAPORT"]

ValueType = Literal["ARRAY", "FALSE", "NULL", "NUMBER", "OBJECT", "STRING", "TRUE"]


@dataclass
class UpdateIcgwPutRequest:
    empty: Optional[bool] = _field(default=None)
    value_type: Optional[ValueType] = _field(
        default=None, metadata={"alias": "valueType"}
    )
