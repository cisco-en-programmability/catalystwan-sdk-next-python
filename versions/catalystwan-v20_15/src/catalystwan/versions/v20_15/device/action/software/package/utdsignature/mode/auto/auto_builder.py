# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class AutoBuilder:
    """
    Builds and executes requests for operations under /device/action/software/package/utdsignature/{type}/mode/auto
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def add_utd_remote_image(self):
        class add_utd_remote_image_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, type_: str, payload: Optional[Any] = None, **kw):
                """
                add Utd remote image

                :param type_: Type
                :param payload: Request body
                :returns: None
                """
                params = {
                    "type": type_,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/device/action/software/package/utdsignature/{type}/mode/auto",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return add_utd_remote_image_(self._request_adapter)
