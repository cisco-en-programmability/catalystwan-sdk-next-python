# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Literal, Optional
from dataclasses import dataclass, field as _field

ValueType = Literal["ARRAY", "FALSE", "NULL", "NUMBER", "OBJECT", "STRING", "TRUE"]


@dataclass
class GetConfigGroupDeviceConfigurationPreviewPostRequest:
    empty: Optional[bool] = _field(default=None)
    value_type: Optional[ValueType] = _field(
        default=None, metadata={"alias": "valueType"}
    )
