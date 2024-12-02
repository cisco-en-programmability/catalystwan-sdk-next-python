# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from catalystwan.abc import RequestAdapterInterface
import logging
from .models import CurrentTimestampResponsePayload


class CurrentTimestampBuilder:
    """
    Builds and executes requests for operations under /stream/device/nwpi/currentTimestamp
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_current_timestamp(self, **kw) -> CurrentTimestampResponsePayload:
        """
        Get current timestamp

        :returns: CurrentTimestampResponsePayload
        """
        logging.warning("Operation: %s is deprecated", "getCurrentTimestamp")
        return self._request_adapter.request(
            "GET",
            "/dataservice/stream/device/nwpi/currentTimestamp",
            return_type=CurrentTimestampResponsePayload,
            **kw,
        )
