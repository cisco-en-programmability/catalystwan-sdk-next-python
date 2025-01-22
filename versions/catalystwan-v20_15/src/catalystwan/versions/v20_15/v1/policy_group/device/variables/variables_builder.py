# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import Default, VariablesDefault

if TYPE_CHECKING:
    from .schema.schema_builder import SchemaBuilder


class VariablesBuilder:
    """
    Builds and executes requests for operations under /v1/policy-group/{policyGroupId}/device/variables
    """

    m = models

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

    def create_policy_group_device_variables(
        self, policy_group_id: str, payload: Optional[Default] = None, **kw
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

    def fetch_policy_group_device_variables(
        self, policy_group_id: str, payload: Optional[VariablesDefault] = None, **kw
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

    @property
    def schema(self) -> SchemaBuilder:
        """
        The schema property
        """
        from .schema.schema_builder import SchemaBuilder

        return SchemaBuilder(self._request_adapter)
