# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from .models import DeviceIp, DeviceModel


class SupportedfeaturesBuilder:
    """
    Builds and executes requests for operations under /device/tools/admintech/supportedfeatures
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_supported_admin_tech_features(self, device_model: DeviceModel, device_ip: DeviceIp, personality: str, **kw):
        """
        Get supported admin tech features

        :param device_model: device Model
        :param device_ip: Device IP
        :param personality: personality
        :returns: None
        """
        params = {
            "deviceModel": device_model,
            "deviceIP": device_ip,
            "personality": personality,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/tools/admintech/supportedfeatures/{deviceModel}/{deviceIP}/{personality}",
            params=params,
            **kw,
        )
