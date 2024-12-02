# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from .models import Codes


class DeviceAuthorizationBuilder:
    """
    Builds and executes requests for operations under /device_authorization
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def device_authorization(self, client_id: str, region_base_uri: str, **kw) -> Codes:
        """
        User authorization for Cisco vManage SecureX integration

        :param client_id: Client id
        :param region_base_uri: Region base uri
        :returns: Codes
        """
        params = {
            "clientId": client_id,
            "regionBaseUri": region_base_uri,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/device_authorization/{regionBaseUri}/{clientId}",
            return_type=Codes,
            params=params,
            **kw,
        )
