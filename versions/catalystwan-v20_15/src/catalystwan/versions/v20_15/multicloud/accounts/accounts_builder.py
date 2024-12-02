# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface
from .models import GetAccounts
from .models import PostAccountsResponse
from .models import PostAccounts
from .models import PutAccounts

if TYPE_CHECKING:
    from .edge.edge_builder import EdgeBuilder
    from .credentials.credentials_builder import CredentialsBuilder


class AccountsBuilder:
    """
    Builds and executes requests for operations under /multicloud/accounts
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_all_cloud_accounts(
        self,
        cloud_type: Optional[str] = None,
        cloud_gateway_enabled: Optional[str] = None,
        **kw,
    ) -> List[GetAccounts]:
        """
        Obtain all accounts for all clouds

        :param cloud_type: Multicloud provider type
        :param cloud_gateway_enabled: Multicloud cloud gateway enabled
        :returns: List[GetAccounts]
        """
        params = {
            "cloudType": cloud_type,
            "cloudGatewayEnabled": cloud_gateway_enabled,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/accounts",
            return_type=List[GetAccounts],
            params=params,
            **kw,
        )

    @property
    def validate_account_add(self):
        class validate_account_add_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[PostAccounts] = None, **kw
            ) -> PostAccountsResponse:
                """
                Add Cloud Account

                :param payload: Payloads for updating Cloud Gateway based on CloudType
                :returns: PostAccountsResponse
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/multicloud/accounts",
                    return_type=PostAccountsResponse,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> PostAccounts:
                return PostAccounts(*args, **kwargs)

            @property
            def payload_model(self) -> Type[PostAccounts]:
                return PostAccounts

        return validate_account_add_(self._request_adapter)

    def get_cloud_account_details(self, account_id: str, **kw) -> GetAccounts:
        """
        Obtain all accounts for all clouds

        :param account_id: Account id
        :returns: GetAccounts
        """
        params = {
            "accountId": account_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/accounts/{accountId}",
            return_type=GetAccounts,
            params=params,
            **kw,
        )

    @property
    def update_account(self):
        class update_account_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, account_id: str, payload: Optional[PutAccounts] = None, **kw
            ):
                """
                Obtain all accounts for all clouds

                :param account_id: Account id
                :param payload: Payloads for updating Cloud Gateway based on CloudType
                :returns: None
                """
                params = {
                    "accountId": account_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/multicloud/accounts/{accountId}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> PutAccounts:
                return PutAccounts(*args, **kwargs)

            @property
            def payload_model(self) -> Type[PutAccounts]:
                return PutAccounts

        return update_account_(self._request_adapter)

    def delete_account(self, account_id: str, **kw):
        """
        Obtain all accounts for all clouds

        :param account_id: Account id
        :returns: None
        """
        params = {
            "accountId": account_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/multicloud/accounts/{accountId}",
            params=params,
            **kw,
        )

    @property
    def credentials(self) -> CredentialsBuilder:
        """
        The credentials property
        """
        from .credentials.credentials_builder import CredentialsBuilder

        return CredentialsBuilder(self._request_adapter)

    @property
    def edge(self) -> EdgeBuilder:
        """
        The edge property
        """
        from .edge.edge_builder import EdgeBuilder

        return EdgeBuilder(self._request_adapter)
