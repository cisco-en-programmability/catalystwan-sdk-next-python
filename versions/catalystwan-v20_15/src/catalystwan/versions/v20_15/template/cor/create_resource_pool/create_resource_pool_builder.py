# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface
import logging


class CreateResourcePoolBuilder:
    """
    Builds and executes requests for operations under /template/cor/createResourcePool
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def create_resource_pool(self):
        class create_resource_pool_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw):
                """
                Add resource pool

                :param payload: Add resource pool request
                :returns: None
                """
                logging.warning("Operation: %s is deprecated", "createResourcePool")
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/template/cor/createResourcePool",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return create_resource_pool_(self._request_adapter)
