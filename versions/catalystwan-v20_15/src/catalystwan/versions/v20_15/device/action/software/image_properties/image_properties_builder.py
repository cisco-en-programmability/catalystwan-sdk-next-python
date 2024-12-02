# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from .models import GetImageProperties


class ImagePropertiesBuilder:
    """
    Builds and executes requests for operations under /device/action/software/imageProperties
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_image_properties(self, version_id: str, **kw) -> GetImageProperties:
        """
        Get Image Properties

        :param version_id: Version id
        :returns: GetImageProperties
        """
        params = {
            "versionId": version_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/action/software/imageProperties/{versionId}",
            return_type=GetImageProperties,
            params=params,
            **kw,
        )
