# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class MultipleBuilder:
    """
    Builds and executes requests for operations under /template/policy/definition/securitygroup/multiple
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def edit_multiple_policy_definition_21(self):
        class edit_multiple_policy_definition_21_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, id: str, payload: Optional[Any] = None, **kw) -> Any:
                """
                Edit multiple policy definitions

                :param id: Policy Id
                :param payload: Policy definition
                :returns: Any
                """
                params = {
                    "id": id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/template/policy/definition/securitygroup/multiple/{id}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return edit_multiple_policy_definition_21_(self._request_adapter)
