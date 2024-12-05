# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import LicensesRequest, LicensesResponse


class LicensesBuilder:
    """
    Builds and executes requests for operations under /v1/licensing/licenses
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_msla_licenses(self):
        class get_msla_licenses_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[LicensesRequest] = None, **kw) -> LicensesResponse:
                """
                Get applicable licenses based on platform class

                :param payload: List of device UUIDs and filters
                :returns: LicensesResponse
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/v1/licensing/licenses", return_type=LicensesResponse, payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> LicensesRequest:
                return LicensesRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[LicensesRequest]:
                return LicensesRequest

        return get_msla_licenses_(self._request_adapter)
