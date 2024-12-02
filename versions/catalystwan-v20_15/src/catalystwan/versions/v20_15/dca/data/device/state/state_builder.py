# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class StateBuilder:
    """
    Builds and executes requests for operations under /dca/data/device/state
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def generate_dca_device_state_data(self):
        class generate_dca_device_state_data_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, state_data_type: str, payload: Optional[Any] = None, **kw
            ) -> Any:
                """
                Get device state data

                :param state_data_type: Device state data
                :param payload: Query string
                :returns: Any
                """
                params = {
                    "state_data_type": state_data_type,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/dca/data/device/state/{state_data_type}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return generate_dca_device_state_data_(self._request_adapter)
