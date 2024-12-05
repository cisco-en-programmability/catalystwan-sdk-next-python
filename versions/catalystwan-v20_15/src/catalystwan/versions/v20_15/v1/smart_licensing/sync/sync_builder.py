# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import SyncRequest


class SyncBuilder:
    """
    Builds and executes requests for operations under /v1/smart-licensing/sync
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def sync_licenses_2(self):
        class sync_licenses_2_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[SyncRequest] = None, **kw):
                """
                Sync licenses from CSSM to vManage db

                :param payload: Partner
                :returns: None
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/v1/smart-licensing/sync", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> SyncRequest:
                return SyncRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[SyncRequest]:
                return SyncRequest

        return sync_licenses_2_(self._request_adapter)
