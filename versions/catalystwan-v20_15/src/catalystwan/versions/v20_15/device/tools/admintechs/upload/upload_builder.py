# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import AdminTechsUploadReq


class UploadBuilder:
    """
    Builds and executes requests for operations under /device/tools/admintechs/upload
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def upload_admin_tech(self):
        class upload_admin_tech_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[AdminTechsUploadReq] = None, **kw):
                """
                upload admin tech to SR

                :param payload: Admin tech upload request
                :returns: None
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/device/tools/admintechs/upload", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> AdminTechsUploadReq:
                return AdminTechsUploadReq(*args, **kwargs)

            @property
            def payload_model(self) -> Type[AdminTechsUploadReq]:
                return AdminTechsUploadReq

        return upload_admin_tech_(self._request_adapter)
