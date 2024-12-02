# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import List, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import SupportedResponse


class SupportedlistBuilder:
    """
    Builds and executes requests for operations under /onboard/supportedlist
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_supported_features(self):
        class get_supported_features_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[List[str]] = None, **kw
            ) -> SupportedResponse:
                """
                Manual Onboard Supported Device features

                :param payload: Manual Onboard Supported Device
                :returns: SupportedResponse
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/onboard/supportedlist",
                    return_type=SupportedResponse,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> List[str]:
                return List[str](*args, **kwargs)

            @property
            def payload_model(self) -> Type[List[str]]:
                return List[str]

        return get_supported_features_(self._request_adapter)
