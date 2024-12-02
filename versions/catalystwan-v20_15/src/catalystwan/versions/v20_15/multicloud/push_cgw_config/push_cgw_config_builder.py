# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import PushCgwConfig, Taskid


class PushCgwConfigBuilder:
    """
    Builds and executes requests for operations under /multicloud/pushCgwConfig
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def push_cgw_cfg(self):
        class push_cgw_cfg_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[PushCgwConfig] = None, **kw) -> Taskid:
                """
                Push configuration to devices of CGW

                :param payload: Push configuration to devices of CGW
                :returns: Taskid
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/multicloud/pushCgwConfig",
                    return_type=Taskid,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> PushCgwConfig:
                return PushCgwConfig(*args, **kwargs)

            @property
            def payload_model(self) -> Type[PushCgwConfig]:
                return PushCgwConfig

        return push_cgw_cfg_(self._request_adapter)
