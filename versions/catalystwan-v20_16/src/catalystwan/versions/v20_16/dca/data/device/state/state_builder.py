# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class StateBuilder:
    """
    Builds and executes requests for operations under /dca/data/device/state
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def generate_dca_device_state_data(
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
