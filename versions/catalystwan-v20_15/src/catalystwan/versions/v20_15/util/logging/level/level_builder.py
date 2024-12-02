# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface
from .models import SetLogLevelPostRequest


class LevelBuilder:
    """
    Builds and executes requests for operations under /util/logging/level
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def set_log_level(self):
        class set_log_level_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[SetLogLevelPostRequest] = None, **kw):
                """
                Set log level for logger

                :param payload: Payload
                :returns: None
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/util/logging/level", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> SetLogLevelPostRequest:
                return SetLogLevelPostRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[SetLogLevelPostRequest]:
                return SetLogLevelPostRequest

        return set_log_level_(self._request_adapter)
