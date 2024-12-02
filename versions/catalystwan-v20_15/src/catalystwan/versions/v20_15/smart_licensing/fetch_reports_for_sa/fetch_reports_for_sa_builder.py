# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class FetchReportsForSaBuilder:
    """
    Builds and executes requests for operations under /smartLicensing/fetchReportsForSa
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def fetch_reports(self):
        class fetch_reports_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, sa_domain: str, sa_id: str, payload: Optional[Any] = None, **kw
            ) -> Any:
                """
                fetch reports offline for sle

                :param sa_domain: saDomain
                :param sa_id: saId
                :param payload: Partner
                :returns: Any
                """
                params = {
                    "saDomain": sa_domain,
                    "saId": sa_id,
                }
                return self._request_adapter.request(
                    "GET",
                    "/dataservice/smartLicensing/fetchReportsForSa",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return fetch_reports_(self._request_adapter)
