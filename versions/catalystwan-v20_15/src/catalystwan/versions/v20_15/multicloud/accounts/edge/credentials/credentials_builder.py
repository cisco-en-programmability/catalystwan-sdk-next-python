# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class CredentialsBuilder:
    """
    Builds and executes requests for operations under /multicloud/accounts/edge/{accountId}/credentials
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def validate_edge_account_update_credentials(self):
        class validate_edge_account_update_credentials_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, account_id: str, payload: Optional[Any] = None, **kw):
                """
                Update Multicloud edge account credential

                :param account_id: Multicloud Edge Account Id
                :param payload: Multicloud edge account info
                :returns: None
                """
                logging.warning(
                    "Operation: %s is deprecated",
                    "validateEdgeAccountUpdateCredentials",
                )
                params = {
                    "accountId": account_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/multicloud/accounts/edge/{accountId}/credentials",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return validate_edge_account_update_credentials_(self._request_adapter)
