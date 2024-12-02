# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface
import logging


class DownBuilder:
    """
    Builds and executes requests for operations under /template/cor/scale/down
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def scale_down(self):
        class scale_down_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw):
                """
                Scale down cloud on ramp

                :param payload: Update VPC
                :returns: None
                """
                logging.warning("Operation: %s is deprecated", "scaleDown")
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/template/cor/scale/down",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return scale_down_(self._request_adapter)
