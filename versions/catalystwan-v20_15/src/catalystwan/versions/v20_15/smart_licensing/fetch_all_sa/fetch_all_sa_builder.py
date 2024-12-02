# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class FetchAllSaBuilder:
    """
    Builds and executes requests for operations under /smartLicensing/fetchAllSa
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def fetch_reports_1(self):
        class fetch_reports_1_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                fetch reports offline for sle

                :param payload: Partner
                :returns: Any
                """
                return self._request_adapter.request(
                    "GET",
                    "/dataservice/smartLicensing/fetchAllSa",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return fetch_reports_1_(self._request_adapter)
