# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Literal, Optional
from dataclasses import dataclass, field as _field

CloudTypeParam = Literal["AWS", "AWS_GOVCLOUD", "AZURE", "AZURE_GOVCLOUD", "GCP"]


@dataclass
class SwImagesResponse:
    device_model: Optional[str] = _field(
        default=None, metadata={"alias": "deviceModel"}
    )
    display_name: Optional[str] = _field(
        default=None, metadata={"alias": "displayName"}
    )
    is_payg_image: Optional[bool] = _field(
        default=None, metadata={"alias": "isPaygImage"}
    )
    software_image_id: Optional[str] = _field(
        default=None, metadata={"alias": "softwareImageId"}
    )
    version: Optional[str] = _field(default=None)
