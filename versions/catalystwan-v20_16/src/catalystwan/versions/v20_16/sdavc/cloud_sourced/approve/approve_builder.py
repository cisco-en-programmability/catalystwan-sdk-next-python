# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import DefaultSuccessResponse, ExtendedApplicationRequestData


class ApproveBuilder:
    """
    Builds and executes requests for operations under /sdavc/cloud-sourced/approve
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def approve_extended_applications(
        self, payload: Optional[ExtendedApplicationRequestData] = None, **kw
    ) -> DefaultSuccessResponse:
        """
        Approve extended applications

        :param payload: Payload
        :returns: DefaultSuccessResponse
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/sdavc/cloud-sourced/approve",
            return_type=DefaultSuccessResponse,
            payload=payload,
            **kw,
        )
