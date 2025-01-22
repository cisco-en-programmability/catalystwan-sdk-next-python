# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import AssociateDefault, Default


class AssociateBuilder:
    """
    Builds and executes requests for operations under /v1/policy-group/{policyGroupId}/device/associate
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_policy_group_association(self, policy_group_id: str, **kw):
        """
        Get devices association with a policy group

        :param policy_group_id: Policy group id
        :returns: None
        """
        params = {
            "policyGroupId": policy_group_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/policy-group/{policyGroupId}/device/associate",
            params=params,
            **kw,
        )

    def update_policy_group_association(
        self, policy_group_id: str, payload: Optional[Default] = None, **kw
    ):
        """
        Move the devices from one policy group to another

        :param policy_group_id: Policy group id
        :param payload: Payload
        :returns: None
        """
        params = {
            "policyGroupId": policy_group_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/policy-group/{policyGroupId}/device/associate",
            params=params,
            payload=payload,
            **kw,
        )

    def create_policy_group_association(
        self, policy_group_id: str, payload: Optional[AssociateDefault] = None, **kw
    ):
        """
        Create associations with device and a policy group

        :param policy_group_id: Policy group id
        :param payload: Payload
        :returns: None
        """
        params = {
            "policyGroupId": policy_group_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/policy-group/{policyGroupId}/device/associate",
            params=params,
            payload=payload,
            **kw,
        )

    def delete_policy_group_association(
        self, policy_group_id: str, payload: Optional[Any] = None, **kw
    ):
        """
        Delete Policy Group Association from devices

        :param policy_group_id: Policy group id
        :param payload: Payload
        :returns: None
        """
        params = {
            "policyGroupId": policy_group_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/policy-group/{policyGroupId}/device/associate",
            params=params,
            payload=payload,
            **kw,
        )
