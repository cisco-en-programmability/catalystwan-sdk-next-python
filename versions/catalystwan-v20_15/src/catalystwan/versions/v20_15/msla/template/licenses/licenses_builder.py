# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface
import logging
from .models import GetSubscriptions1PostRequest


class LicensesBuilder:
    """
    Builds and executes requests for operations under /msla/template/licenses
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_subscriptions_1(self):
        class get_subscriptions_1_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[GetSubscriptions1PostRequest] = None, **kw
            ) -> Any:
                """
                Retrieve MSLA subscription/licenses

                :param payload: Payload
                :returns: Any
                """
                logging.warning("Operation: %s is deprecated", "getSubscriptions_1")
                return self._request_adapter.request(
                    "POST", "/dataservice/msla/template/licenses", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> GetSubscriptions1PostRequest:
                return GetSubscriptions1PostRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[GetSubscriptions1PostRequest]:
                return GetSubscriptions1PostRequest

        return get_subscriptions_1_(self._request_adapter)
