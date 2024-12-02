# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface
from .models import FormPostResp


class FileuploadBuilder:
    """
    Builds and executes requests for operations under /system/device/fileupload
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def form_post(self):
        class form_post_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> FormPostResp:
                """
                Upload file to vEdge

                :param payload: Request body for Upload file to vEdge
                :returns: FormPostResp
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/system/device/fileupload",
                    return_type=FormPostResp,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return form_post_(self._request_adapter)
