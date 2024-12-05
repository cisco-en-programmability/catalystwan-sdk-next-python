# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import List

from catalystwan.abc import RequestAdapterInterface

from .models import NwpiNbarAppGroupResponsePayloadInner


class NwpiNbarAppGroupBuilder:
    """
    Builds and executes requests for operations under /stream/device/nwpi/nwpiNbarAppGroup
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_nwpi_nbar_app_group(self, **kw) -> List[NwpiNbarAppGroupResponsePayloadInner]:
        """
        Get nwpi nbar app group

        :returns: List[NwpiNbarAppGroupResponsePayloadInner]
        """
        logging.warning("Operation: %s is deprecated", "getNwpiNbarAppGroup")
        return self._request_adapter.request(
            "GET",
            "/dataservice/stream/device/nwpi/nwpiNbarAppGroup",
            return_type=List[NwpiNbarAppGroupResponsePayloadInner],
            **kw,
        )
