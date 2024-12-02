# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface
from .models import InterconnectAccount


class CredentialsBuilder:
    """
    Builds and executes requests for operations under /multicloud/interconnect/accounts/{interconnect-account-id}/credentials
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def update_interconnect_account_credentials(self):
        class update_interconnect_account_credentials_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                interconnect_account_id: str,
                payload: Optional[InterconnectAccount] = None,
                **kw,
            ) -> InterconnectAccount:
                """
                API to edit associated Interconnect provider account credentials.

                :param interconnect_account_id: Interconnect provider account id
                :param payload: Request Payload for Multicloud Interconnect Accounts
                :returns: InterconnectAccount
                """
                params = {
                    "interconnect-account-id": interconnect_account_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/multicloud/interconnect/accounts/{interconnect-account-id}/credentials",
                    return_type=InterconnectAccount,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> InterconnectAccount:
                return InterconnectAccount(*args, **kwargs)

            @property
            def payload_model(self) -> Type[InterconnectAccount]:
                return InterconnectAccount

        return update_interconnect_account_credentials_(self._request_adapter)
