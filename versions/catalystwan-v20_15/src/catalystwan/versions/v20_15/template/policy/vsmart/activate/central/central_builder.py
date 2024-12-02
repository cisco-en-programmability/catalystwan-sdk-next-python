# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class CentralBuilder:
    """
    Builds and executes requests for operations under /template/policy/vsmart/activate/central
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def activate_policy_for_cloud_services(self):
        class activate_policy_for_cloud_services_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, policy_id: str, payload: Optional[Any] = None, **kw
            ) -> Any:
                """
                Activate vsmart policy for a given policy id

                :param policy_id: Policy Id
                :param payload: Template policy
                :returns: Any
                """
                params = {
                    "policyId": policy_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/template/policy/vsmart/activate/central/{policyId}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return activate_policy_for_cloud_services_(self._request_adapter)
