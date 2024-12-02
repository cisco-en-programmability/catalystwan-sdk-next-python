# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from catalystwan.abc import RequestAdapterInterface
from .models import SdaDevicesRes


class DeviceBuilder:
    """
    Builds and executes requests for operations under /partner/dnac/sda/device
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sda_enabled_devices(self, partner_id: str, **kw) -> SdaDevicesRes:
        """
        Get SDA enabled devices

        :param partner_id: Partner id
        :returns: SdaDevicesRes
        """
        params = {
            "partnerId": partner_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/partner/dnac/sda/device/{partnerId}",
            return_type=SdaDevicesRes,
            params=params,
            **kw,
        )

    def get_device_details(self, partner_id: str, uuid: str, **kw) -> SdaDevicesRes:
        """
        Get SDA enabled devices detail

        :param partner_id: Partner id
        :param uuid: Uuid
        :returns: SdaDevicesRes
        """
        params = {
            "partnerId": partner_id,
            "uuid": uuid,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/partner/dnac/sda/device/{partnerId}/{uuid}",
            return_type=SdaDevicesRes,
            params=params,
            **kw,
        )
