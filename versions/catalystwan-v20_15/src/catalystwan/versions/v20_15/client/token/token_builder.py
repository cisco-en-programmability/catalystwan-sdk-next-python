# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from .models import ClientTokenResponse


class TokenBuilder:
    """
    Builds and executes requests for operations under /client/token
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_csrf_token(self, json: Optional[bool] = False, **kw) -> ClientTokenResponse:
        """
        Get CSRF token

        :param json: Json
        :returns: ClientTokenResponse
        """
        params = {
            "json": json,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/client/token",
            return_type=ClientTokenResponse,
            params=params,
            **kw,
        )
