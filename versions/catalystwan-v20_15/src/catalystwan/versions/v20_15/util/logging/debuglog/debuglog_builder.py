# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import DebugLogPostRequest


class DebuglogBuilder:
    """
    Builds and executes requests for operations under /util/logging/debuglog
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def debug_log(self):
        class debug_log_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[DebugLogPostRequest] = None, **kw):
                """
                Test whether logging works

                :param payload: Payload
                :returns: None
                """
                logging.warning("Operation: %s is deprecated", "debugLog")
                return self._request_adapter.request(
                    "POST", "/dataservice/util/logging/debuglog", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> DebugLogPostRequest:
                return DebugLogPostRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[DebugLogPostRequest]:
                return DebugLogPostRequest

        return debug_log_(self._request_adapter)
