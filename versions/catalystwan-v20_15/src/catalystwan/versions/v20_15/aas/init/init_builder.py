# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import InitBlob


class InitBuilder:
    """
    Builds and executes requests for operations under /aas/init
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def init_aas_properties(self):
        class init_aas_properties_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[InitBlob] = None, **kw):
                """
                Initialize SDWAN as a Platform

                :param payload: Payload
                :returns: None
                """
                return self._request_adapter.request("POST", "/dataservice/aas/init", payload=payload, **kw)

            def create_payload(self, *args, **kwargs) -> InitBlob:
                return InitBlob(*args, **kwargs)

            @property
            def payload_model(self) -> Type[InitBlob]:
                return InitBlob

        return init_aas_properties_(self._request_adapter)
