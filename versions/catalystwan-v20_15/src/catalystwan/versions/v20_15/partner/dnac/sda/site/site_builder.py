# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from .models import SdaSitesRes


class SiteBuilder:
    """
    Builds and executes requests for operations under /partner/dnac/sda/site
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sites_for_partner(self, partner_id: str, **kw) -> SdaSitesRes:
        """
        Get SDA Sites for Partner

        :param partner_id: Partner id
        :returns: SdaSitesRes
        """
        params = {
            "partnerId": partner_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/partner/dnac/sda/site/{partnerId}",
            return_type=SdaSitesRes,
            params=params,
            **kw,
        )
