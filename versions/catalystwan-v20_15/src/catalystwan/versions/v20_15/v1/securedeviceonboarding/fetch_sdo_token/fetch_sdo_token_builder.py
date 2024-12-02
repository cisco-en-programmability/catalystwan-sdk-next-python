# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import DetailsForIdentityVerificationForSdoToken


class FetchSdoTokenBuilder:
    """
    Builds and executes requests for operations under /v1/securedeviceonboarding/fetchSdoToken
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def fetch_sdo_token(self):
        class fetch_sdo_token_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                payload: Optional[DetailsForIdentityVerificationForSdoToken] = None,
                **kw,
            ):
                """
                POST for fetching Secure Device Onboarding Token needed for Secure Device Onboarding APIs for eSim

                :param payload: Fetch SDO Token
                :returns: None
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/securedeviceonboarding/fetchSdoToken",
                    payload=payload,
                    **kw,
                )

            def create_payload(
                self, *args, **kwargs
            ) -> DetailsForIdentityVerificationForSdoToken:
                return DetailsForIdentityVerificationForSdoToken(*args, **kwargs)

            @property
            def payload_model(self) -> Type[DetailsForIdentityVerificationForSdoToken]:
                return DetailsForIdentityVerificationForSdoToken

        return fetch_sdo_token_(self._request_adapter)
