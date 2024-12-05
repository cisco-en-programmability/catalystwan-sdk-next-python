# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import InterconnectAccount

if TYPE_CHECKING:
    from .billing_accounts.billing_accounts_builder import BillingAccountsBuilder
    from .cloud.cloud_builder import CloudBuilder
    from .connectivity.connectivity_builder import ConnectivityBuilder
    from .credentials.credentials_builder import CredentialsBuilder
    from .locations.locations_builder import LocationsBuilder


class AccountsBuilder:
    """
    Builds and executes requests for operations under /multicloud/interconnect/accounts
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_interconnect_accounts(self, interconnect_type: Optional[str] = None, **kw) -> List[InterconnectAccount]:
        """
        API to retrieve Interconnect provider accounts.

        :param interconnect_type: Interconnect provider type
        :returns: List[InterconnectAccount]
        """
        params = {
            "interconnect-type": interconnect_type,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/interconnect/accounts",
            return_type=List[InterconnectAccount],
            params=params,
            **kw,
        )

    @property
    def add_interconnect_account(self):
        class add_interconnect_account_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[InterconnectAccount] = None, **kw) -> InterconnectAccount:
                """
                API to associate an Interconnect provider account to vManage.

                :param payload: Request Payload for Multicloud Interconnect Accounts
                :returns: InterconnectAccount
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/multicloud/interconnect/accounts",
                    return_type=InterconnectAccount,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> InterconnectAccount:
                return InterconnectAccount(*args, **kwargs)

            @property
            def payload_model(self) -> Type[InterconnectAccount]:
                return InterconnectAccount

        return add_interconnect_account_(self._request_adapter)

    def get_interconnect_account(self, interconnect_account_id: str, **kw) -> InterconnectAccount:
        """
        API to retrieve associated Interconnect provider account details by id.

        :param interconnect_account_id: Interconnect provider account id
        :returns: InterconnectAccount
        """
        params = {
            "interconnect-account-id": interconnect_account_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/interconnect/accounts/{interconnect-account-id}",
            return_type=InterconnectAccount,
            params=params,
            **kw,
        )

    @property
    def update_interconnect_account(self):
        class update_interconnect_account_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, interconnect_account_id: str, payload: Optional[InterconnectAccount] = None, **kw):
                """
                API to edit associated Interconnect provider account name and description.

                :param interconnect_account_id: Interconnect provider account id
                :param payload: Request Payload for Multicloud Interconnect Accounts
                :returns: None
                """
                params = {
                    "interconnect-account-id": interconnect_account_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/multicloud/interconnect/accounts/{interconnect-account-id}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> InterconnectAccount:
                return InterconnectAccount(*args, **kwargs)

            @property
            def payload_model(self) -> Type[InterconnectAccount]:
                return InterconnectAccount

        return update_interconnect_account_(self._request_adapter)

    def delete_interconnect_account(self, interconnect_account_id: str, **kw):
        """
        API to disassociate Interconnect provider account from vManage.

        :param interconnect_account_id: Interconnect provider account id
        :returns: None
        """
        params = {
            "interconnect-account-id": interconnect_account_id,
        }
        return self._request_adapter.request(
            "DELETE", "/dataservice/multicloud/interconnect/accounts/{interconnect-account-id}", params=params, **kw
        )

    @property
    def billing_accounts(self) -> BillingAccountsBuilder:
        """
        The billing-accounts property
        """
        from .billing_accounts.billing_accounts_builder import BillingAccountsBuilder

        return BillingAccountsBuilder(self._request_adapter)

    @property
    def cloud(self) -> CloudBuilder:
        """
        The cloud property
        """
        from .cloud.cloud_builder import CloudBuilder

        return CloudBuilder(self._request_adapter)

    @property
    def connectivity(self) -> ConnectivityBuilder:
        """
        The connectivity property
        """
        from .connectivity.connectivity_builder import ConnectivityBuilder

        return ConnectivityBuilder(self._request_adapter)

    @property
    def credentials(self) -> CredentialsBuilder:
        """
        The credentials property
        """
        from .credentials.credentials_builder import CredentialsBuilder

        return CredentialsBuilder(self._request_adapter)

    @property
    def locations(self) -> LocationsBuilder:
        """
        The locations property
        """
        from .locations.locations_builder import LocationsBuilder

        return LocationsBuilder(self._request_adapter)
