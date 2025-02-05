# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .validate.validate_builder import ValidateBuilder


class PasswordBuilder:
    """
    Builds and executes requests for operations under /admin/user/password
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def update_password_1(self, user_name: str, payload: Optional[Any] = None, **kw):
        """
        Update user password

        :param user_name: User name
        :param payload: User
        :returns: None
        """
        params = {
            "userName": user_name,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/admin/user/password/{userName}",
            params=params,
            payload=payload,
            **kw,
        )

    @property
    def validate(self) -> ValidateBuilder:
        """
        The validate property
        """
        from .validate.validate_builder import ValidateBuilder

        return ValidateBuilder(self._request_adapter)
