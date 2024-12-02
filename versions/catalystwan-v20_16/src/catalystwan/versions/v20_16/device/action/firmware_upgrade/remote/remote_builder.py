# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import ProcessFirmwareRemoteImageReq, ProcessGetFirmwareRemoteImageReq


class RemoteBuilder:
    """
    Builds and executes requests for operations under /device/action/firmware-upgrade/remote
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_firmware_remote_image(self, **kw) -> ProcessGetFirmwareRemoteImageReq:
        """
        firmware remote image package

        :returns: ProcessGetFirmwareRemoteImageReq
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/action/firmware-upgrade/remote",
            return_type=ProcessGetFirmwareRemoteImageReq,
            **kw,
        )

    def process_firmware_remote_image(
        self, payload: Optional[Any] = None, **kw
    ) -> ProcessFirmwareRemoteImageReq:
        """
        firmware remote image package

        :param payload: Request body
        :returns: ProcessFirmwareRemoteImageReq
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/device/action/firmware-upgrade/remote",
            return_type=ProcessFirmwareRemoteImageReq,
            payload=payload,
            **kw,
        )

    def edit_firmware_upgarde_remote_image(
        self, version_id: str, payload: Optional[Any] = None, **kw
    ) -> ProcessGetFirmwareRemoteImageReq:
        """
        Download software package file

        :param version_id: Version id
        :param payload: Request body
        :returns: ProcessGetFirmwareRemoteImageReq
        """
        params = {
            "versionId": version_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/device/action/firmware-upgrade/remote/{versionId}",
            return_type=ProcessGetFirmwareRemoteImageReq,
            params=params,
            payload=payload,
            **kw,
        )
