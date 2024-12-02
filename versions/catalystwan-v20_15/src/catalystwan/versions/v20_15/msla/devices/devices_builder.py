# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import List, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import GetDeviceLicensesInner, GetMslaDevicesPayload, ReleaseLicensesRequest


class DevicesBuilder:
    """
    Builds and executes requests for operations under /msla/devices
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_msla_devices_1(
        self, site_id: Optional[str] = None, **kw
    ) -> GetMslaDevicesPayload:
        """
        Retrieve list of devices and their subscription information

        :param site_id: Site id
        :returns: GetMslaDevicesPayload
        """
        params = {
            "site-id": site_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/msla/devices",
            return_type=GetMslaDevicesPayload,
            params=params,
            **kw,
        )

    @property
    def release_licenses_1(self):
        class release_licenses_1_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[ReleaseLicensesRequest] = None, **kw):
                """
                Release licenses assigned to the devices

                :param payload: List of devices for unassigning licenses
                :returns: None
                """
                return self._request_adapter.request(
                    "PUT", "/dataservice/msla/devices", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> ReleaseLicensesRequest:
                return ReleaseLicensesRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[ReleaseLicensesRequest]:
                return ReleaseLicensesRequest

        return release_licenses_1_(self._request_adapter)

    def get_license_by_uuid_1(self, uuid: str, **kw) -> List[GetDeviceLicensesInner]:
        """
        Get licenses associated to device

        :param uuid: Uuid
        :returns: List[GetDeviceLicensesInner]
        """
        params = {
            "uuid": uuid,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/msla/devices/{uuid}",
            return_type=List[GetDeviceLicensesInner],
            params=params,
            **kw,
        )
