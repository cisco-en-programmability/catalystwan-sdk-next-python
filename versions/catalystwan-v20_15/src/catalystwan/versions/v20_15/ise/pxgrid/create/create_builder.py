# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import CreateBody, CreateResponse


class CreateBuilder:
    """
    Builds and executes requests for operations under /ise/pxgrid/create
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def account_create(self, payload: Optional[CreateBody] = None, **kw) -> CreateResponse:
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
