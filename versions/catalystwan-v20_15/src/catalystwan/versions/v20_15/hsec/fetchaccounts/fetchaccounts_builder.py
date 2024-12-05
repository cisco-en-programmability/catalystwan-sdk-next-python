# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import FetchAccounts1PostRequest, SmartLicensingfetchAccountsResp


class FetchaccountsBuilder:
    """
    Builds and executes requests for operations under /hsec/fetchaccounts
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def fetch_sava_accounts(
        self, username: Optional[str] = None, pwd: Optional[str] = None, mode: Optional[str] = None, **kw
    ) -> SmartLicensingfetchAccountsResp:
        """
        Authenticate User and Sync Licenses

        :param username: Username
        :param pwd: Pwd
        :param mode: Mode
        :returns: SmartLicensingfetchAccountsResp
        """
        params = {
            "username": username,
            "pwd": pwd,
            "mode": mode,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/hsec/fetchaccounts", return_type=SmartLicensingfetchAccountsResp, params=params, **kw
        )

    @property
    def fetch_accounts_1(self):
        class fetch_accounts_1_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[FetchAccounts1PostRequest] = None, **kw
            ) -> SmartLicensingfetchAccountsResp:
                """
                Authenticate User and Sync Licenses

                :param payload: Hsec License sync request payload
                :returns: SmartLicensingfetchAccountsResp
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/hsec/fetchaccounts",
                    return_type=SmartLicensingfetchAccountsResp,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> FetchAccounts1PostRequest:
                return FetchAccounts1PostRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[FetchAccounts1PostRequest]:
                return FetchAccounts1PostRequest

        return fetch_accounts_1_(self._request_adapter)
