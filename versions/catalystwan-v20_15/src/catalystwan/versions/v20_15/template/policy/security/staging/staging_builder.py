# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class StagingBuilder:
    """
    Builds and executes requests for operations under /template/policy/security/staging
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def edit_template_with_lenient_lock(self):
        class edit_template_with_lenient_lock_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
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

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return edit_template_with_lenient_lock_(self._request_adapter)
