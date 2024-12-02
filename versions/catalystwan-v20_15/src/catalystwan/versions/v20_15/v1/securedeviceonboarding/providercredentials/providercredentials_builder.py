# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface
from .models import ProviderAccountDetails


class ProvidercredentialsBuilder:
    """
    Builds and executes requests for operations under /v1/securedeviceonboarding/providercredentials
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def create_provider_credentials(self):
        class create_provider_credentials_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[ProviderAccountDetails] = None, **kw):
                """
                Create service provider credentials

                :param payload: Create Provider Credentials
                :returns: None
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/securedeviceonboarding/providercredentials",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> ProviderAccountDetails:
                return ProviderAccountDetails(*args, **kwargs)

            @property
            def payload_model(self) -> Type[ProviderAccountDetails]:
                return ProviderAccountDetails

        return create_provider_credentials_(self._request_adapter)

    def get_provider_credentials_by_account_id(self, account_id: str, **kw) -> str:
        """
        Get provider credentials by account id

        :param account_id: Service User Account ID
        :returns: str
        """
        params = {
            "accountId": account_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/securedeviceonboarding/{accountId}/providercredentials",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_provider_credentials(self):
        class edit_provider_credentials_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                account_id: str,
                payload: Optional[ProviderAccountDetails] = None,
                **kw,
            ):
                """
                Edit service provider credentials

                :param account_id: Service User Account ID
                :param payload: Provider Credentials
                :returns: None
                """
                params = {
                    "accountId": account_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/securedeviceonboarding/{accountId}/providercredentials",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> ProviderAccountDetails:
                return ProviderAccountDetails(*args, **kwargs)

            @property
            def payload_model(self) -> Type[ProviderAccountDetails]:
                return ProviderAccountDetails

        return edit_provider_credentials_(self._request_adapter)
