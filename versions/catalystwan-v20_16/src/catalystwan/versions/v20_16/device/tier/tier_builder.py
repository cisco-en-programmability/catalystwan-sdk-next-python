# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface


class TierBuilder:
    """
    Builds and executes requests for operations under /device/tier
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_tiers(self, **kw):
        """
        getTiers

        :returns: None
        """
        return self._request_adapter.request("GET", "/dataservice/device/tier", **kw)

    def add_tier(self, add_tier: str, **kw):
        """
        add tier

        :param add_tier: addTier
        :returns: None
        """
        params = {
            "addTier": add_tier,
        }
        return self._request_adapter.request(
            "POST", "/dataservice/device/tier", params=params, **kw
        )

    def delete_tier(self, tier_name: str, **kw):
        """
        deleteTier

        :param tier_name: deletetier
        :returns: None
        """
        params = {
            "tierName": tier_name,
        }
        return self._request_adapter.request(
            "DELETE", "/dataservice/device/tier/{tierName}", params=params, **kw
        )
