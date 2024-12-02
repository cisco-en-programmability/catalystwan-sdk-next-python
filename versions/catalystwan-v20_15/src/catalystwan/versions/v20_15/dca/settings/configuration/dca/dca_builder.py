# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import TypeParam


class DcaBuilder:
    """
    Builds and executes requests for operations under /dca/settings/configuration/{type}/dca
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def create_dca_analytics_data_file(self):
        class create_dca_analytics_data_file_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, type_: TypeParam, payload: Optional[Any] = None, **kw
            ) -> Any:
                """
                Create analytics config data

                :param type_: Data type
                :param payload: Query string
                :returns: Any
                """
                params = {
                    "type": type_,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/dca/settings/configuration/{type}/dca",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return create_dca_analytics_data_file_(self._request_adapter)
