# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class BulkBuilder:
    """
    Builds and executes requests for operations under /template/policy/definition/vpnqosmap/bulk
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def save_policy_definition_in_bulk_2(self):
        class save_policy_definition_in_bulk_2_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Create/Edit policy definitions in bulk

                :param payload: Policy definition
                :returns: Any
                """
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/template/policy/definition/vpnqosmap/bulk",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return save_policy_definition_in_bulk_2_(self._request_adapter)
