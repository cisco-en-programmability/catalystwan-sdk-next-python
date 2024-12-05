# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional

from catalystwan.abc import RequestAdapterInterface


class CentralBuilder:
    """
    Builds and executes requests for operations under /template/policy/vsmart/central
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def edit_template_without_lock_checks(self, policy_id: str, payload: Optional[Any] = None, **kw) -> List[Any]:
        """
        Edit template for given policy id to allow for multiple component edits

        :param policy_id: Policy Id
        :param payload: Template policy
        :returns: List[Any]
        """
        params = {
            "policyId": policy_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/template/policy/vsmart/central/{policyId}",
            return_type=List[Any],
            params=params,
            payload=payload,
            **kw,
        )
