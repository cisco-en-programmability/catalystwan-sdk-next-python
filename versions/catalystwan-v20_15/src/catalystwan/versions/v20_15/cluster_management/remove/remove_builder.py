# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class RemoveBuilder:
    """
    Builds and executes requests for operations under /clusterManagement/remove
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def remove_vmanage(self):
        class remove_vmanage_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw):
                """
                Remove vManage from cluster


                Note: In a multitenant vManage system, this API is only available in the Provider view.

                :param payload: vManage server info
                :returns: None
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/clusterManagement/remove",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return remove_vmanage_(self._request_adapter)
