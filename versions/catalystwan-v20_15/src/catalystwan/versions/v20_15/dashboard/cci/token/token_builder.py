# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional
from catalystwan.abc import RequestAdapterInterface


class TokenBuilder:
    """
    Builds and executes requests for operations under /dashboard/cci/token
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def cci_token(self, device_code: Optional[str] = None, **kw):
        """
        Get CCI token after Complete CCI Login

        :param device_code: device code authenticated
        :returns: None
        """
        params = {
            "deviceCode": device_code,
        }
        return self._request_adapter.request(
            "POST", "/dataservice/dashboard/cci/token", params=params, **kw
        )
