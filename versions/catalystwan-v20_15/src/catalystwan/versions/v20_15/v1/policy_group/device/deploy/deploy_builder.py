# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import DeployPolicyGroupPostRequest, DeployPolicyGroupPostResponse


class DeployBuilder:
    """
    Builds and executes requests for operations under /v1/policy-group/{policyGroupId}/device/deploy
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def deploy_policy_group(
        self, policy_group_id: str, payload: Optional[DeployPolicyGroupPostRequest] = None, **kw
    ) -> DeployPolicyGroupPostResponse:
        """
        deploy policy group to devices

        :param policy_group_id: Policy Group Id
        :param payload: Payload
        :returns: DeployPolicyGroupPostResponse
        """
        params = {
            "policyGroupId": policy_group_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/policy-group/{policyGroupId}/device/deploy",
            return_type=DeployPolicyGroupPostResponse,
            params=params,
            payload=payload,
            **kw,
        )
