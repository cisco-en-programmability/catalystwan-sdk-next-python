# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface
from .models import CreateResponse
from .models import CreateBody


class CreateBuilder:
    """
    Builds and executes requests for operations under /ise/pxgrid/create
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def account_create(self):
        class account_create_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[CreateBody] = None, **kw
            ) -> CreateResponse:
                """
                Create pxGrid account

                :param payload: name for pxgrid node
                :returns: CreateResponse
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/ise/pxgrid/create",
                    return_type=CreateResponse,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> CreateBody:
                return CreateBody(*args, **kwargs)

            @property
            def payload_model(self) -> Type[CreateBody]:
                return CreateBody

        return account_create_(self._request_adapter)
