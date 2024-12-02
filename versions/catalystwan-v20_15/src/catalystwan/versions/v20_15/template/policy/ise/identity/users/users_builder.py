# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface
from .models import UsersResponse
from .models import UsersBody


class UsersBuilder:
    """
    Builds and executes requests for operations under /template/policy/ise/identity/users
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_identity_users(self):
        class get_identity_users_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[UsersBody] = None, **kw
            ) -> UsersResponse:
                """
                Get all identity users

                :param payload: Get Users from ISE associated with Active Directory Domain. Body can be empty object or null to return all users. For filtering can be like the example with a regex or a specific user.
                :returns: UsersResponse
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/template/policy/ise/identity/users",
                    return_type=UsersResponse,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> UsersBody:
                return UsersBody(*args, **kwargs)

            @property
            def payload_model(self) -> Type[UsersBody]:
                return UsersBody

        return get_identity_users_(self._request_adapter)
