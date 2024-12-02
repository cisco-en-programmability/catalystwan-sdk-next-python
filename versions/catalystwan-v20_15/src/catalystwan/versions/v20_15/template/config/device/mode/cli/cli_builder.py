# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List, Any, Type
from catalystwan.abc import RequestAdapterInterface
from .models import TypeParam


class CliBuilder:
    """
    Builds and executes requests for operations under /template/config/device/mode/cli
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def generate_cli_mode_devices(self, type_: TypeParam, **kw) -> List[Any]:
        """
        Generates a JSON object that contains a list of valid devices in CLI mode

        :param type_: Device type
        :returns: List[Any]
        """
        params = {
            "type": type_,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/template/config/device/mode/cli",
            return_type=List[Any],
            params=params,
            **kw,
        )

    @property
    def update_device_to_cli_mode(self):
        class update_device_to_cli_mode_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Given a JSON list of devices not managed by any third member partners, push to devices from a CLI template

                :param payload: Device list
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/template/config/device/mode/cli",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return update_device_to_cli_mode_(self._request_adapter)
