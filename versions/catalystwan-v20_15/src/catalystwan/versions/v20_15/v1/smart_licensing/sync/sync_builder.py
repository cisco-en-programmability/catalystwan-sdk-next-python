# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import SyncRequest


class SyncBuilder:
    """
    Builds and executes requests for operations under /v1/smart-licensing/sync
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def sync_licenses_2(self, payload: Optional[SyncRequest] = None, **kw):
        """
        Sync licenses from CSSM to vManage db

        :param payload: Partner
        :returns: None
        """
        return self._request_adapter.request(
            "POST", "/dataservice/v1/smart-licensing/sync", payload=payload, **kw
        )
