# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface


class GetBiFrostSigningKeyBuilder:
    """
    Builds and executes requests for operations under /dashboard/getBiFrostSigningKey
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_bi_frost_signing_key(self, cd_client_token: Optional[str] = None, **kw):
        """
        Register Controller to BiFrost Dashboard (by Controller)

        :param cd_client_token: CD client token
        :returns: None
        """
        params = {
            "cdClientToken": cd_client_token,
        }
        return self._request_adapter.request("GET", "/dataservice/dashboard/getBiFrostSigningKey", params=params, **kw)
