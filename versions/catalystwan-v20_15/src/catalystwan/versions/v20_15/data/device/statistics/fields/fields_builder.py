# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import List, Any
from catalystwan.abc import RequestAdapterInterface


class FieldsBuilder:
    """
    Builds and executes requests for operations under /data/device/statistics/{state_data_type}/fields
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_stat_data_fields_by_state_data_type(
        self, state_data_type: str, **kw
    ) -> List[Any]:
        """
        Get statistics fields and types

        :param state_data_type: State data type
        :returns: List[Any]
        """
        params = {
            "state_data_type": state_data_type,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/data/device/statistics/{state_data_type}/fields",
            return_type=List[Any],
            params=params,
            **kw,
        )
