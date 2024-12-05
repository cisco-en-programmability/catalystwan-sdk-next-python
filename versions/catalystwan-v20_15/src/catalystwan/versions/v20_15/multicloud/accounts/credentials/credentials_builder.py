# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import PostAccounts, PostAccountsResponse


class CredentialsBuilder:
    """
    Builds and executes requests for operations under /multicloud/accounts/{accountId}/credentials
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def validate_account_update_credentials(self):
        class validate_account_update_credentials_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, account_id: str, payload: Optional[PostAccounts] = None, **kw) -> PostAccountsResponse:
                """
                Update Cloud Account Credentials

                :param account_id: Account id
                :param payload: Payloads for updating Cloud Gateway based on CloudType
                :returns: PostAccountsResponse
                """
                params = {
                    "accountId": account_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/multicloud/accounts/{accountId}/credentials",
                    return_type=PostAccountsResponse,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> PostAccounts:
                return PostAccounts(*args, **kwargs)

            @property
            def payload_model(self) -> Type[PostAccounts]:
                return PostAccounts

        return validate_account_update_credentials_(self._request_adapter)
