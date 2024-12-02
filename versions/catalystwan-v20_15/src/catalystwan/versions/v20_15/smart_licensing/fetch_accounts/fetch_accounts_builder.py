# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import SmartLicensingfetchAccountsResp


class FetchAccountsBuilder:
    """
    Builds and executes requests for operations under /smartLicensing/fetchAccounts
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def fetch_accounts(self):
        class fetch_accounts_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, mode: str, payload: Optional[Any] = None, **kw
            ) -> SmartLicensingfetchAccountsResp:
                """
                fetch sava for sle

                :param mode: mode
                :param payload: Partner
                :returns: SmartLicensingfetchAccountsResp
                """
                params = {
                    "mode": mode,
                }
                return self._request_adapter.request(
                    "GET",
                    "/dataservice/smartLicensing/fetchAccounts",
                    return_type=SmartLicensingfetchAccountsResp,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return fetch_accounts_(self._request_adapter)
