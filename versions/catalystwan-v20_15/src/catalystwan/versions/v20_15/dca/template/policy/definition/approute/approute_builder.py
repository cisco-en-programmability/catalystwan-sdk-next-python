# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class ApprouteBuilder:
    """
    Builds and executes requests for operations under /dca/template/policy/definition/approute
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_template_policy_definitions_dca(self):
        class get_template_policy_definitions_dca_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> List[Any]:
                """
                Get template policy definitions

                :param payload: Query string
                :returns: List[Any]
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/dca/template/policy/definition/approute",
                    return_type=List[Any],
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return get_template_policy_definitions_dca_(self._request_adapter)
