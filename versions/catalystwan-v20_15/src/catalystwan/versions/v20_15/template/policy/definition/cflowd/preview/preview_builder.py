# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class PreviewBuilder:
    """
    Builds and executes requests for operations under /template/policy/definition/cflowd/preview
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def preview_policy_definition_13(self):
        class preview_policy_definition_13_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Preview policy definition

                :param payload: Policy definition
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/template/policy/definition/cflowd/preview",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return preview_policy_definition_13_(self._request_adapter)

    def preview_policy_definition_by_id_13(self, id: str, **kw) -> Any:
        """
        Preview policy definition

        :param id: Policy Id
        :returns: Any
        """
        params = {
            "id": id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/template/policy/definition/cflowd/preview/{id}",
            params=params,
            **kw,
        )
