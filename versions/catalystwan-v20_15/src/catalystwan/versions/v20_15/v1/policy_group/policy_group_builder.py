# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import CreatePolicyGroupPostRequest, CreatePolicyGroupPostResponse, PolicyGroup

if TYPE_CHECKING:
    from .device.device_builder import DeviceBuilder


class PolicyGroupBuilder:
    """
    Builds and executes requests for operations under /v1/policy-group
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_policy_group_by_solution(
        self, solution: Optional[str] = None, **kw
    ) -> List[PolicyGroup]:
        """
        Get a Policy Group by Solution

        :param solution: Solution
        :returns: List[PolicyGroup]
        """
        params = {
            "solution": solution,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/policy-group",
            return_type=List[PolicyGroup],
            params=params,
            **kw,
        )

    def create_policy_group(
        self, payload: Optional[CreatePolicyGroupPostRequest] = None, **kw
    ) -> CreatePolicyGroupPostResponse:
        """
        Create a new Policy Group

        :param payload: Policy Group
        :returns: CreatePolicyGroupPostResponse
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/policy-group",
            return_type=CreatePolicyGroupPostResponse,
            payload=payload,
            **kw,
        )

    def get_policy_group(self, policy_group_id: str, **kw) -> PolicyGroup:
        """
        Get a Policy Group by ID

        :param policy_group_id: Policy group id
        :returns: PolicyGroup
        """
        params = {
            "policyGroupId": policy_group_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/policy-group/{policyGroupId}",
            return_type=PolicyGroup,
            params=params,
            **kw,
        )

    def edit_policy_group(self, policy_group_id: str, payload: Optional[str] = None, **kw) -> str:
        """
        Edit a Policy Group

        :param policy_group_id: Policy group id
        :param payload: Policy Group
        :returns: str
        """
        params = {
            "policyGroupId": policy_group_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/policy-group/{policyGroupId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_policy_group(
        self, policy_group_id: str, delete_profiles: Optional[bool] = None, **kw
    ):
        """
        Delete Policy Group

        :param policy_group_id: Policy group id
        :param delete_profiles: Delete profiles
        :returns: None
        """
        params = {
            "policyGroupId": policy_group_id,
            "deleteProfiles": delete_profiles,
        }
        return self._request_adapter.request(
            "DELETE", "/dataservice/v1/policy-group/{policyGroupId}", params=params, **kw
        )

    @property
    def device(self) -> DeviceBuilder:
        """
        The device property
        """
        from .device.device_builder import DeviceBuilder

        return DeviceBuilder(self._request_adapter)
