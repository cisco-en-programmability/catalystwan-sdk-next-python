# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface
from .models import ClaimDevicesResponse
from .models import ClaimDevicesRequest


class ClaimDevicesBuilder:
    """
    Builds and executes requests for operations under /system/device/claimDevices
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def claim_devices(self):
        class claim_devices_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[ClaimDevicesRequest] = None, **kw
            ) -> ClaimDevicesResponse:
                """
                Claim the selected unclaimed devices

                :param payload: Claim device request
                :returns: ClaimDevicesResponse
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/system/device/claimDevices",
                    return_type=ClaimDevicesResponse,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> ClaimDevicesRequest:
                return ClaimDevicesRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[ClaimDevicesRequest]:
                return ClaimDevicesRequest

        return claim_devices_(self._request_adapter)
