# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import ActivateBody, ActivateResponse


class ActivateBuilder:
    """
    Builds and executes requests for operations under /ise/pxgrid/activate
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def account_activate(self):
        class account_activate_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[ActivateBody] = None, **kw) -> ActivateResponse:
                """
                Activate pxGrid account

                :param payload: description for pxgrid node
                :returns: ActivateResponse
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/ise/pxgrid/activate", return_type=ActivateResponse, payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> ActivateBody:
                return ActivateBody(*args, **kwargs)

            @property
            def payload_model(self) -> Type[ActivateBody]:
                return ActivateBody

        return account_activate_(self._request_adapter)
