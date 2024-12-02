# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class SetupBuilder:
    """
    Builds and executes requests for operations under /clusterManagement/setup
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def edit_vmanage(self):
        class edit_vmanage_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw):
                """
                Update vManage cluster info


                Note: In a multitenant vManage system, this API is only available in the Provider view.

                :param payload: vManage cluster config
                :returns: None
                """
                return self._request_adapter.request(
                    "PUT", "/dataservice/clusterManagement/setup", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return edit_vmanage_(self._request_adapter)

    @property
    def add_vmanage(self):
        class add_vmanage_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw):
                """
                Add vManage to cluster

                :param payload: vManage cluster config
                :returns: None
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/clusterManagement/setup",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return add_vmanage_(self._request_adapter)
