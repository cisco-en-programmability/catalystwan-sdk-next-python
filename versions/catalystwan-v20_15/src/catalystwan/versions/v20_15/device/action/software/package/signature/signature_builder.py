# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from catalystwan.abc import RequestAdapterInterface
from .models import ImageData
from .models import UtdsignatureParam


class SignatureBuilder:
    """
    Builds and executes requests for operations under /device/action/software/package/signature
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def generate_utd_image_data(
        self, utdsignature: UtdsignatureParam, type_: str, **kw
    ) -> ImageData:
        """
        Get list of Utd images

        :param utdsignature: utdsignature
        :param type_: Type
        :returns: ImageData
        """
        params = {
            "utdsignature": utdsignature,
            "type": type_,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/action/software/package/signature/{utdsignature}",
            return_type=ImageData,
            params=params,
            **kw,
        )
