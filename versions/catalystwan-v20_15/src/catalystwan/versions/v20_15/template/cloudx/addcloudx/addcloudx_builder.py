# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface
import logging


class AddcloudxBuilder:
    """
    Builds and executes requests for operations under /template/cloudx/addcloudx
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def add_cloudx_type(self):
        class add_cloudx_type_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, type_: str, payload: Optional[Any] = None, **kw):
                """
                Add cloudx gateway

                :param type_: Cloudx type
                :param payload: Cloudx
                :returns: None
                """
                logging.warning("Operation: %s is deprecated", "addCloudxType")
                params = {
                    "type": type_,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/template/cloudx/addcloudx/{type}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return add_cloudx_type_(self._request_adapter)
