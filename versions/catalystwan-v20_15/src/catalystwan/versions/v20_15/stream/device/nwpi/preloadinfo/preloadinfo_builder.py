# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from .models import NwpiPreloadRespPayload


class PreloadinfoBuilder:
    """
    Builds and executes requests for operations under /stream/device/nwpi/preloadinfo
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_preload_info(
        self, mode: Optional[str] = None, **kw
    ) -> NwpiPreloadRespPayload:
        """
        Get preload info

        :param mode: mode
        :returns: NwpiPreloadRespPayload
        """
        logging.warning("Operation: %s is deprecated", "getPreloadInfo")
        params = {
            "mode": mode,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/stream/device/nwpi/preloadinfo",
            return_type=NwpiPreloadRespPayload,
            params=params,
            **kw,
        )
