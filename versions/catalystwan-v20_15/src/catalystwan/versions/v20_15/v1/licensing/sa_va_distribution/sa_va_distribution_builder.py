# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface
from .models import SaVaDistributionResponse
from .models import SaVaDistributionRequest


class SaVaDistributionBuilder:
    """
    Builds and executes requests for operations under /v1/licensing/sa-va-distribution
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_sava_distribution(self):
        class get_sava_distribution_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
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

            def create_payload(self, *args, **kwargs) -> SaVaDistributionRequest:
                return SaVaDistributionRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[SaVaDistributionRequest]:
                return SaVaDistributionRequest

        return get_sava_distribution_(self._request_adapter)
