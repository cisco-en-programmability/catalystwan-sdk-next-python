# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List, Any, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface
from .models import DeviceIp
from .models import TaskId

if TYPE_CHECKING:
    from .devices.devices_builder import DevicesBuilder


class RebootBuilder:
    """
    Builds and executes requests for operations under /device/action/reboot
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def generate_reboot_info(self, device_id: List[DeviceIp], **kw) -> List[Any]:
        """
        Get device reboot information

        :param device_id: Device Id
        :returns: List[Any]
        """
        params = {
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/action/reboot",
            return_type=List[Any],
            params=params,
            **kw,
        )

    @property
    def process_reboot(self):
        class process_reboot_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> TaskId:
                """
                Process a reboot operation

                :param payload: Device reboot request payload
                :returns: TaskId
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/device/action/reboot",
                    return_type=TaskId,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return process_reboot_(self._request_adapter)

    @property
    def devices(self) -> DevicesBuilder:
        """
        The devices property
        """
        from .devices.devices_builder import DevicesBuilder

        return DevicesBuilder(self._request_adapter)
