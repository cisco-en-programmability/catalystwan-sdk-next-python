# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface
from .models import ProcessGetFirmwareRemoteImageReq
from .models import ProcessFirmwareRemoteImageReq


class RemoteBuilder:
    """
    Builds and executes requests for operations under /device/action/firmware-upgrade/remote
    """

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

    @property
    def process_firmware_remote_image(self):
        class process_firmware_remote_image_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[Any] = None, **kw
            ) -> ProcessFirmwareRemoteImageReq:
                """
                firmware remote image package

                :param payload: Request body for Device bootstrap configuration
                :returns: ProcessFirmwareRemoteImageReq
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/device/action/firmware-upgrade/remote",
                    return_type=ProcessFirmwareRemoteImageReq,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return process_firmware_remote_image_(self._request_adapter)

    @property
    def edit_firmware_upgarde_remote_image(self):
        class edit_firmware_upgarde_remote_image_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
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

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return edit_firmware_upgarde_remote_image_(self._request_adapter)
