# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import AdminTechReq


class CopyBuilder:
    """
    Builds and executes requests for operations under /device/tools/admintech/copy
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def copy_admin_tech_on_device(self):
        class copy_admin_tech_on_device_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[AdminTechReq] = None, **kw):
                """
                copy admin tech logs

                :param payload: Admin tech copy request
                :returns: None
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/device/tools/admintech/copy",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> AdminTechReq:
                return AdminTechReq(*args, **kwargs)

            @property
            def payload_model(self) -> Type[AdminTechReq]:
                return AdminTechReq

        return copy_admin_tech_on_device_(self._request_adapter)
