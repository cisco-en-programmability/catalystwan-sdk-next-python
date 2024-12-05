# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class PreviewBuilder:
    """
    Builds and executes requests for operations under /template/policy/definition/dnssecurity/preview
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def preview_policy_definition(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Preview policy definition

        :param payload: Policy definition
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/template/policy/definition/dnssecurity/preview", payload=payload, **kw
        )

    def preview_policy_definition_by_id(self, id: str, **kw) -> Any:
        """
        Preview policy definition

        :param id: Policy Id
        :returns: Any
        """
        params = {
            "id": id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/template/policy/definition/dnssecurity/preview/{id}", params=params, **kw
        )
