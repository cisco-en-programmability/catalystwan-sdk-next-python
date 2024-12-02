# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import UserGroupsBody, UserGroupsResponse


class UsergroupsBuilder:
    """
    Builds and executes requests for operations under /template/policy/ise/identity/usergroups
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_identity_user_groups(self):
        class get_identity_user_groups_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[UserGroupsBody] = None, **kw
            ) -> UserGroupsResponse:
                """
                Get all identity user groups

                :param payload: Get Users Groups from ISE associated with Active Directory Domain. Body can be an empty object or null to return all User Groups. For filtering a group must be specified, you cannot use a regex.
                :returns: UserGroupsResponse
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/template/policy/ise/identity/usergroups",
                    return_type=UserGroupsResponse,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> UserGroupsBody:
                return UserGroupsBody(*args, **kwargs)

            @property
            def payload_model(self) -> Type[UserGroupsBody]:
                return UserGroupsBody

        return get_identity_user_groups_(self._request_adapter)
