# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from catalystwan.abc import RequestAdapterInterface


class GoogleMapKeyBuilder:
    """
    Builds and executes requests for operations under /settings/configuration/googleMapKey
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_google_map_key(self, **kw) -> str:
        """
        Retrieve Google map key

        :returns: str
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/settings/configuration/googleMapKey",
            return_type=str,
            **kw,
        )
