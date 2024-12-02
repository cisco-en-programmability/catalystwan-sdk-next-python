# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class ImageDownloadBuilder:
    """
    Builds and executes requests for operations under /device/action/image-download
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def initiate_image_download(self):
        class initiate_image_download_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw):
                """
                Intitate image download on the given device.

                :param payload: Request body to Intitate image download on the given device
                :returns: None
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/device/action/image-download",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return initiate_image_download_(self._request_adapter)
