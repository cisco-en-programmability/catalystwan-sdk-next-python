# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class StagingBuilder:
    """
    Builds and executes requests for operations under /template/policy/security/staging
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def edit_template_with_lenient_lock(
        self, policy_id: str, payload: Optional[Any] = None, **kw
    ) -> Any:
        """
        Edit Template

        :param policy_id: Policy Id
        :param payload: Policy template
        :returns: Any
        """
        params = {
            "policyId": policy_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/template/policy/security/staging/{policyId}",
            params=params,
            payload=payload,
            **kw,
        )
