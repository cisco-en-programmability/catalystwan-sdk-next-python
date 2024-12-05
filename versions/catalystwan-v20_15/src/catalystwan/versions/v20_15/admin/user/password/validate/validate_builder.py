# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class ValidateBuilder:
    """
    Builds and executes requests for operations under /admin/user/password/validate
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def validate_password_1(self, payload: Optional[Any] = None, **kw):
        """
        Validate user password

        :param payload: User password
        :returns: None
        """
        return self._request_adapter.request("POST", "/dataservice/admin/user/password/validate", payload=payload, **kw)
