# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from catalystwan.abc import RequestAdapterInterface

from .models import GenerateDeviceStateData

if TYPE_CHECKING:
    from .fields.fields_builder import FieldsBuilder
    from .query.query_builder import QueryBuilder


class StateBuilder:
    """
    Builds and executes requests for operations under /data/device/state
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def generate_device_state_data(
        self, state_data_type: str, start_id: Optional[str] = None, count: Optional[int] = 1000, **kw
    ) -> GenerateDeviceStateData:
        """
        Get device state data

        :param state_data_type: State data type
        :param start_id: Start id
        :param count: Count
        :returns: GenerateDeviceStateData
        """
        params = {
            "state_data_type": state_data_type,
            "startId": start_id,
            "count": count,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/data/device/state/{state_data_type}",
            return_type=GenerateDeviceStateData,
            params=params,
            **kw,
        )

    @property
    def fields(self) -> FieldsBuilder:
        """
        The fields property
        """
        from .fields.fields_builder import FieldsBuilder

        return FieldsBuilder(self._request_adapter)

    @property
    def query(self) -> QueryBuilder:
        """
        The query property
        """
        from .query.query_builder import QueryBuilder

        return QueryBuilder(self._request_adapter)
