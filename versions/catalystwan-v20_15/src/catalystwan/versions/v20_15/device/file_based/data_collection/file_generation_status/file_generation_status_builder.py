# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import HandleFileGenerationStatusNotificationRequest


class FileGenerationStatusBuilder:
    """
    Builds and executes requests for operations under /device/file-based/data-collection/file-generation-status
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def handle_file_generation_status_response_from_device(self):
        class handle_file_generation_status_response_from_device_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[HandleFileGenerationStatusNotificationRequest] = None, **kw):
                """
                Device notify when file is ready and vManage has to download them

                :param payload: File generation status notification payload
                :returns: None
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/device/file-based/data-collection/file-generation-status",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> HandleFileGenerationStatusNotificationRequest:
                return HandleFileGenerationStatusNotificationRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[HandleFileGenerationStatusNotificationRequest]:
                return HandleFileGenerationStatusNotificationRequest

        return handle_file_generation_status_response_from_device_(self._request_adapter)
