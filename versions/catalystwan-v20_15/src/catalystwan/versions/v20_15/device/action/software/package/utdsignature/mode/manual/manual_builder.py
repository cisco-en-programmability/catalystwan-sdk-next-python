# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface
from .models import InstallPkg


class ManualBuilder:
    """
    Builds and executes requests for operations under /device/action/software/package/utdsignature/{type}/mode/manual
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def upload_utd_image(self):
        class upload_utd_image_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, type_: str, payload: Optional[InstallPkg] = None, **kw):
                """
                upload Utd image

                :param type_: Type
                :param payload: Utd image File
                :returns: None
                """
                params = {
                    "type": type_,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/device/action/software/package/utdsignature/{type}/mode/manual",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> InstallPkg:
                return InstallPkg(*args, **kwargs)

            @property
            def payload_model(self) -> Type[InstallPkg]:
                return InstallPkg

        return upload_utd_image_(self._request_adapter)
