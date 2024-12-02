# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List, Type
from catalystwan.abc import RequestAdapterInterface
from .models import AdminTechListRes
from .models import AdminTechListReq


class AdmintechlistBuilder:
    """
    Builds and executes requests for operations under /device/tools/admintechlist
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def list_admin_techs_on_device(self):
        class list_admin_techs_on_device_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[AdminTechListReq] = None, **kw
            ) -> List[AdminTechListRes]:
                """
                List admin tech logs

                :param payload: Admin tech listing request
                :returns: List[AdminTechListRes]
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/device/tools/admintechlist",
                    return_type=List[AdminTechListRes],
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> AdminTechListReq:
                return AdminTechListReq(*args, **kwargs)

            @property
            def payload_model(self) -> Type[AdminTechListReq]:
                return AdminTechListReq

        return list_admin_techs_on_device_(self._request_adapter)
