# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import GenerateRediscoverInfo


class RediscoverBuilder:
    """
    Builds and executes requests for operations under /device/action/rediscover
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def generate_rediscover_info(self, **kw) -> GenerateRediscoverInfo:
        """
        Get rediscover operation information

        :returns: GenerateRediscoverInfo
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/action/rediscover",
            return_type=GenerateRediscoverInfo,
            **kw,
        )

    @property
    def re_discover_devices(self):
        class re_discover_devices_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw):
                """
                Rediscover device

                :param payload: Rediscover device request payload
                :returns: None
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/device/action/rediscover",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return re_discover_devices_(self._request_adapter)
