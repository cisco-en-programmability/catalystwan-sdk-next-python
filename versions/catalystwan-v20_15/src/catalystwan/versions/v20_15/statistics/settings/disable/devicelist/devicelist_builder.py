# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class DevicelistBuilder:
    """
    Builds and executes requests for operations under /statistics/settings/disable/devicelist
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_disabled_device_list(self, index_name: str, **kw) -> Any:
        """
        Get list of disabled devices for a statistics index

        :param index_name: Index name
        :returns: Any
        """
        params = {
            "indexName": index_name,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/statistics/settings/disable/devicelist/{indexName}",
            params=params,
            **kw,
        )

    @property
    def update_statistics_device_list(self):
        class update_statistics_device_list_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, index_name: str, payload: Optional[Any] = None, **kw
            ) -> Any:
                """
                Update list of disabled devices for a statistics index

                :param index_name: Index name
                :param payload: Disabled device
                :returns: Any
                """
                params = {
                    "indexName": index_name,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/statistics/settings/disable/devicelist/{indexName}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return update_statistics_device_list_(self._request_adapter)
