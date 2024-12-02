# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface
import logging


class DetachBuilder:
    """
    Builds and executes requests for operations under /template/device/config/detach
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def detach_device_template(self):
        class detach_device_template_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw):
                """
                Detach device template


                Note: In a multitenant vManage system, this API is only available in the Provider view.

                :param payload: Device template
                :returns: None
                """
                logging.warning("Operation: %s is deprecated", "detachDeviceTemplate")
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/template/device/config/detach",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return detach_device_template_(self._request_adapter)
