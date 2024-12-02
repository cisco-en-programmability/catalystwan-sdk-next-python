# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface


class InitiatePolicyComplianceBuilder:
    """
    Builds and executes requests for operations under /sdavc/protocol-pack/compliance/initiate-policy-compliance
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def initiate_policy_compliance(self, **kw):
        """
        Initiate policy compliance task

        :returns: None
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/sdavc/protocol-pack/compliance/initiate-policy-compliance",
            **kw,
        )
