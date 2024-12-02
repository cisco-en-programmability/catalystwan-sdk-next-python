# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface
import logging


class UpBuilder:
    """
    Builds and executes requests for operations under /template/cor/scale/up
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def scale_up(self):
        class scale_up_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw):
                """
                Scale up cloud on ramp

                :param payload: Update VPC
                :returns: None
                """
                logging.warning("Operation: %s is deprecated", "scaleUp")
                return self._request_adapter.request(
                    "POST", "/dataservice/template/cor/scale/up", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return scale_up_(self._request_adapter)
