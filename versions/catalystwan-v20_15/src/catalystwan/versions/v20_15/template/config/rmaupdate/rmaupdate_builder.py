# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class RmaupdateBuilder:
    """
    Builds and executes requests for operations under /template/config/rmaupdate
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def rma_update(self):
        class rma_update_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw):
                """
                Update new device

                :param payload: Template config
                :returns: None
                """
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/template/config/rmaupdate",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return rma_update_(self._request_adapter)
