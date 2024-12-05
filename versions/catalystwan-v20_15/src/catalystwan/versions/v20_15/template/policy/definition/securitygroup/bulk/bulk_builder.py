# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class BulkBuilder:
    """
    Builds and executes requests for operations under /template/policy/definition/securitygroup/bulk
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def save_policy_definition_in_bulk_21(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Create/Edit policy definitions in bulk

        :param payload: Policy definition
        :returns: Any
        """
        return self._request_adapter.request(
            "PUT", "/dataservice/template/policy/definition/securitygroup/bulk", payload=payload, **kw
        )
