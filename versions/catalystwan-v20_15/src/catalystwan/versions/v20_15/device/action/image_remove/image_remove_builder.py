# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class ImageRemoveBuilder:
    """
    Builds and executes requests for operations under /device/action/image-remove
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def process_remove_software_image(self, payload: Optional[Any] = None, **kw):
        """
        Process remove software image operation

        :param payload: Request body - Process remove software image operation
        :returns: None
        """
        return self._request_adapter.request("POST", "/dataservice/device/action/image-remove", payload=payload, **kw)
