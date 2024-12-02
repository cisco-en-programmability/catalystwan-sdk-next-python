# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface
from .models import DeployPolicyGroupPostRequest


class DeployBuilder:
    """
    Builds and executes requests for operations under /v1/policy-group/{policyGroupId}/device/deploy
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def deploy_policy_group(self):
        class deploy_policy_group_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                policy_group_id: str,
                payload: Optional[DeployPolicyGroupPostRequest] = None,
                **kw,
            ) -> Any:
                """
                deploy policy group to devices

                :param policy_group_id: Policy Group Id
                :param payload: Payload
                :returns: Any
                """
                params = {
                    "policyGroupId": policy_group_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/policy-group/{policyGroupId}/device/deploy",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> DeployPolicyGroupPostRequest:
                return DeployPolicyGroupPostRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[DeployPolicyGroupPostRequest]:
                return DeployPolicyGroupPostRequest

        return deploy_policy_group_(self._request_adapter)
