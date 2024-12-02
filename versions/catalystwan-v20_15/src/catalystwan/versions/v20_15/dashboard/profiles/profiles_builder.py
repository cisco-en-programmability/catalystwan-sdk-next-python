# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import ClaimStatusParam, SigningKey


class ProfilesBuilder:
    """
    Builds and executes requests for operations under /dashboard/profiles
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def list_cd_profiles(self, claim_status: Optional[ClaimStatusParam] = None, **kw):
        """
        Retrieve CD profiles from CRS

        :param claim_status: claim status used to query CD profiles
        :returns: None
        """
        params = {
            "claimStatus": claim_status,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/dashboard/profiles", params=params, **kw
        )

    @property
    def update_bi_frost_info(self):
        class update_bi_frost_info_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[SigningKey] = None, **kw):
                """
                Update BiFrost Dashboard Info (by BiFrost)

                :param payload: Client identification
                :returns: None
                """
                return self._request_adapter.request(
                    "PUT", "/dataservice/dashboard/profiles", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> SigningKey:
                return SigningKey(*args, **kwargs)

            @property
            def payload_model(self) -> Type[SigningKey]:
                return SigningKey

        return update_bi_frost_info_(self._request_adapter)
