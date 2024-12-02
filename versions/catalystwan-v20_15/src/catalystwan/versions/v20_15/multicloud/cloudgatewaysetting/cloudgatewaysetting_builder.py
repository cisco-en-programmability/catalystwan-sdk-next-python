# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from catalystwan.abc import RequestAdapterInterface
from .models import CustomSettings


class CloudgatewaysettingBuilder:
    """
    Builds and executes requests for operations under /multicloud/cloudgatewaysetting
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_cgw_custom_setting_details(
        self, cloud_gateway_name: str, **kw
    ) -> CustomSettings:
        """
        Get cloud gateway custom setting by cloud gateway name

        :param cloud_gateway_name: Cloud gateway name
        :returns: CustomSettings
        """
        params = {
            "cloudGatewayName": cloud_gateway_name,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/cloudgatewaysetting/{cloudGatewayName}",
            return_type=CustomSettings,
            params=params,
            **kw,
        )
