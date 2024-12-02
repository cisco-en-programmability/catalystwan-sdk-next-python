# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Type

from catalystwan.abc import RequestAdapterInterface

from .models import SdaConfigRequest, SdaDeviceConfigRes


class ConfigBuilder:
    """
    Builds and executes requests for operations under /partner/dnac/sda/config
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def create_sda_config(self):
        class create_sda_config_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, partner_id: str, payload: SdaConfigRequest, **kw
            ) -> SdaDeviceConfigRes:
                """
                Create SDA enabled device

                :param partner_id: Partner id
                :param payload: Device SDA configuration
                :returns: SdaDeviceConfigRes
                """
                params = {
                    "partnerId": partner_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/partner/dnac/sda/config/{partnerId}",
                    return_type=SdaDeviceConfigRes,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> SdaConfigRequest:
                return SdaConfigRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[SdaConfigRequest]:
                return SdaConfigRequest

        return create_sda_config_(self._request_adapter)
