# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class ImageDownloadBuilder:
    """
    Builds and executes requests for operations under /device/action/image-download
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def initiate_image_download(self, payload: Optional[Any] = None, **kw):
        """
        Intitate image download on the given device.

        :param payload: Request body to Intitate image download on the given device
        :returns: None
        """
        return self._request_adapter.request(
            "POST", "/dataservice/device/action/image-download", payload=payload, **kw
        )
