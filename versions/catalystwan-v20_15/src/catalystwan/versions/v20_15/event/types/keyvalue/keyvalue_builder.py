# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import SimpleKeyValueMapping


class KeyvalueBuilder:
    """
    Builds and executes requests for operations under /event/types/keyvalue
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_event_types_as_key_value(self, **kw) -> SimpleKeyValueMapping:
        """
        Get event types.

        :returns: SimpleKeyValueMapping
        """
        return self._request_adapter.request(
            "GET", "/dataservice/event/types/keyvalue", return_type=SimpleKeyValueMapping, **kw
        )
