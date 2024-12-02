# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class RuleBuilder:
    """
    Builds and executes requests for operations under /notifications/rule
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def update_notification_rule(self):
        class update_notification_rule_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, rule_id: str, payload: Optional[Any] = None, **kw):
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
                    "PUT",
                    "/dataservice/notifications/rule",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return update_notification_rule_(self._request_adapter)

    @property
    def create_notification_rule(self):
        class create_notification_rule_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw):
                """
                Add notification rule

                :param payload: Notification rule
                :returns: None
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/notifications/rule", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return create_notification_rule_(self._request_adapter)
