# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import SubmitDay0ConfigPostRequest


class SubmitDevicesBuilder:
    """
    Builds and executes requests for operations under /template/config/quickConnect/submitDevices
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def submit_day0_config(self):
        class submit_day0_config_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[SubmitDay0ConfigPostRequest] = None, **kw
            ) -> List[Any]:
                """
                Creates and pushes bootstrap configurations onto day0 devices.

                :param payload: Payload
                :returns: List[Any]
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/template/config/quickConnect/submitDevices",
                    return_type=List[Any],
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> SubmitDay0ConfigPostRequest:
                return SubmitDay0ConfigPostRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[SubmitDay0ConfigPostRequest]:
                return SubmitDay0ConfigPostRequest

        return submit_day0_config_(self._request_adapter)
