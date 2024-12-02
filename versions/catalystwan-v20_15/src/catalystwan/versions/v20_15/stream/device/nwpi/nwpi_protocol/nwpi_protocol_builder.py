# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import List

from catalystwan.abc import RequestAdapterInterface

from .models import NwpiProtocolResponsePayloadInner


class NwpiProtocolBuilder:
    """
    Builds and executes requests for operations under /stream/device/nwpi/nwpiProtocol
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_nwpi_protocol(self, **kw) -> List[NwpiProtocolResponsePayloadInner]:
        """
        Get nwpi protocol

        :returns: List[NwpiProtocolResponsePayloadInner]
        """
        logging.warning("Operation: %s is deprecated", "getNwpiProtocol")
        return self._request_adapter.request(
            "GET",
            "/dataservice/stream/device/nwpi/nwpiProtocol",
            return_type=List[NwpiProtocolResponsePayloadInner],
            **kw,
        )
