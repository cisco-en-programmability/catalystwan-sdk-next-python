# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface
from .models import CreatePolicyGroupDeviceVariablesPutRequest

if TYPE_CHECKING:
    from .schema.schema_builder import SchemaBuilder


class VariablesBuilder:
    """
    Builds and executes requests for operations under /v1/policy-group/{policyGroupId}/device/variables
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_policy_group_device_variables(
        self,
        policy_group_id: str,
        device_id: Optional[str] = None,
        suggestions: Optional[bool] = None,
        **kw,
    ) -> Any:
        """
        Get device variables

        :param policy_group_id: Policy Group Id
        :param device_id: Comma separated device id's like d1,d2
        :param suggestions: Suggestions for possible values
        :returns: Any
        """
        params = {
            "policyGroupId": policy_group_id,
            "device-id": device_id,
            "suggestions": suggestions,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/policy-group/{policyGroupId}/device/variables",
            params=params,
            **kw,
        )

    @property
    def create_policy_group_device_variables(self):
        class create_policy_group_device_variables_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                policy_group_id: str,
                payload: Optional[CreatePolicyGroupDeviceVariablesPutRequest] = None,
                **kw,
            ) -> Any:
                """
                assign values to device variables

                :param policy_group_id: Policy Group Id
                :param payload: Payload
                :returns: Any
                """
                params = {
                    "policyGroupId": policy_group_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/policy-group/{policyGroupId}/device/variables",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(
                self, *args, **kwargs
            ) -> CreatePolicyGroupDeviceVariablesPutRequest:
                return CreatePolicyGroupDeviceVariablesPutRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[CreatePolicyGroupDeviceVariablesPutRequest]:
                return CreatePolicyGroupDeviceVariablesPutRequest

        return create_policy_group_device_variables_(self._request_adapter)

    @property
    def fetch_policy_group_device_variables(self):
        class fetch_policy_group_device_variables_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                policy_group_id: str,
                payload: Optional[CreatePolicyGroupDeviceVariablesPutRequest] = None,
                **kw,
            ) -> Any:
                """
                Fetch device variables

                :param policy_group_id: Policy Group Id
                :param payload: Payload
                :returns: Any
                """
                params = {
                    "policyGroupId": policy_group_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/policy-group/{policyGroupId}/device/variables",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(
                self, *args, **kwargs
            ) -> CreatePolicyGroupDeviceVariablesPutRequest:
                return CreatePolicyGroupDeviceVariablesPutRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[CreatePolicyGroupDeviceVariablesPutRequest]:
                return CreatePolicyGroupDeviceVariablesPutRequest

        return fetch_policy_group_device_variables_(self._request_adapter)

    @property
    def schema(self) -> SchemaBuilder:
        """
        The schema property
        """
        from .schema.schema_builder import SchemaBuilder

        return SchemaBuilder(self._request_adapter)
