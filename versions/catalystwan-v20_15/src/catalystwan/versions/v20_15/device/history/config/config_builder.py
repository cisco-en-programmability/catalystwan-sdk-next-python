# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .diff.diff_builder import DiffBuilder


class ConfigBuilder:
    """
    Builds and executes requests for operations under /device/history/config
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_last_thousand_config_list(self, device_id: str, query: str, **kw) -> Any:
        """
        Get device config history

        :param device_id: Device Id
        :param query: Query filter
        :returns: Any
        """
        params = {
            "deviceId": device_id,
            "query": query,
        }
        return self._request_adapter.request("GET", "/dataservice/device/history/config", params=params, **kw)

    def get_device_config(self, config_id: str, **kw) -> Any:
        """
        Get device config

        :param config_id: Config Id
        :returns: Any
        """
        params = {
            "config_id": config_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/device/history/config/{config_id}", params=params, **kw
        )

    @property
    def diff(self) -> DiffBuilder:
        """
        The diff property
        """
        from .diff.diff_builder import DiffBuilder

        return DiffBuilder(self._request_adapter)
