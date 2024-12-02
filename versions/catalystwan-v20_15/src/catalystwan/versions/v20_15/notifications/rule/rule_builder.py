# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class RuleBuilder:
    """
    Builds and executes requests for operations under /notifications/rule
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def update_notification_rule(self, rule_id: str, payload: Optional[Any] = None, **kw):
        """
        Update notification rule

        :param rule_id: Rule Id
        :param payload: Notification rule
        :returns: None
        """
        params = {
            "ruleId": rule_id,
        }
        return self._request_adapter.request(
            "PUT", "/dataservice/notifications/rule", params=params, payload=payload, **kw
        )

    def create_notification_rule(self, payload: Optional[Any] = None, **kw):
        """
        Add notification rule

        :param payload: Notification rule
        :returns: None
        """
        return self._request_adapter.request(
            "POST", "/dataservice/notifications/rule", payload=payload, **kw
        )
