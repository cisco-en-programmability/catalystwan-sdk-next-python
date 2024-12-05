# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import UpdatePreUpgradeCheckStatusPutRequest


class CheckBuilder:
    """
    Builds and executes requests for operations under /device/action/status/preupgrade/check
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def update_pre_upgrade_check_status(self):
        class update_pre_upgrade_check_status_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[UpdatePreUpgradeCheckStatusPutRequest] = None, **kw):
                """
                Update pre upgrade check status

                :param payload: Payload
                :returns: None
                """
                return self._request_adapter.request(
                    "PUT", "/dataservice/device/action/status/preupgrade/check", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> UpdatePreUpgradeCheckStatusPutRequest:
                return UpdatePreUpgradeCheckStatusPutRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[UpdatePreUpgradeCheckStatusPutRequest]:
                return UpdatePreUpgradeCheckStatusPutRequest

        return update_pre_upgrade_check_status_(self._request_adapter)
