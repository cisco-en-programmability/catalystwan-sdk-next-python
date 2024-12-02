# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any

from catalystwan.abc import RequestAdapterInterface


class UserAuthTypeBuilder:
    """
    Builds and executes requests for operations under /admin/user/userAuthType
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def find_user_auth_type_1(self, **kw) -> Any:
        """
        Find user authentication type, whether it is SAML enabled

        :returns: Any
        """
        return self._request_adapter.request(
            "GET", "/dataservice/admin/user/userAuthType", **kw
        )
