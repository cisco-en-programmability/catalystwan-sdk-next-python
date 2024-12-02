# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import UpdatePreUpgradeCheckStatusPutRequest


class CheckBuilder:
    """
    Builds and executes requests for operations under /device/action/status/preupgrade/check
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def update_pre_upgrade_check_status(
        self, payload: Optional[UpdatePreUpgradeCheckStatusPutRequest] = None, **kw
    ):
        """
        Update pre upgrade check status

        :param payload: Payload
        :returns: None
        """
        return self._request_adapter.request(
            "PUT", "/dataservice/device/action/status/preupgrade/check", payload=payload, **kw
        )
