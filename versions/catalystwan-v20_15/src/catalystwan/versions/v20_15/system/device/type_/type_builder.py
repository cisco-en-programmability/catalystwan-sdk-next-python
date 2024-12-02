# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, List

from catalystwan.abc import RequestAdapterInterface

from .models import DeviceCategoryParam

if TYPE_CHECKING:
    from .default_config.default_config_builder import DefaultConfigBuilder


class TypeBuilder:
    """
    Builds and executes requests for operations under /system/device/type
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_cloud_dock_data_based_on_device_type(
        self, device_category: DeviceCategoryParam, **kw
    ) -> List[Any]:
        """
        Get devices details

        :param device_category: Device category
        :returns: List[Any]
        """
        logging.warning(
            "Operation: %s is deprecated", "getCloudDockDataBasedOnDeviceType"
        )
        params = {
            "deviceCategory": device_category,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/system/device/type/{deviceCategory}",
            return_type=List[Any],
            params=params,
            **kw,
        )

    @property
    def default_config(self) -> DefaultConfigBuilder:
        """
        The defaultConfig property
        """
        from .default_config.default_config_builder import DefaultConfigBuilder

        return DefaultConfigBuilder(self._request_adapter)
