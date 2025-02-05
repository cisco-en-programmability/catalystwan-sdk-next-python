# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import SaVaDistributionRequest, SaVaDistributionResponse


class SaVaDistributionBuilder:
    """
    Builds and executes requests for operations under /v1/licensing/sa-va-distribution
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sava_distribution(
        self, payload: Optional[SaVaDistributionRequest] = None, **kw
    ) -> SaVaDistributionResponse:
        """
        Get Smart account and virtual account distribution of selected licenses

        :param payload: Payload
        :returns: SaVaDistributionResponse
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/licensing/sa-va-distribution",
            return_type=SaVaDistributionResponse,
            payload=payload,
            **kw,
        )
