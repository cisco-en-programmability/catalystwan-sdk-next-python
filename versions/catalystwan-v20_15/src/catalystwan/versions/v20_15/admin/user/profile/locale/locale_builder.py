# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class LocaleBuilder:
    """
    Builds and executes requests for operations under /admin/user/profile/locale
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def update_profile_locale_1(self, payload: Optional[Any] = None, **kw):
        """
        Update profile locale

        :param payload: User
        :returns: None
        """
        return self._request_adapter.request(
            "PUT", "/dataservice/admin/user/profile/locale", payload=payload, **kw
        )
