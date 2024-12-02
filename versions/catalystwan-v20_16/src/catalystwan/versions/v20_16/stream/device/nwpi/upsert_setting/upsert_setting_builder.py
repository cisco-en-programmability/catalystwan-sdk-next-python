# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import NwpiSettingDataPayload


class UpsertSettingBuilder:
    """
    Builds and executes requests for operations under /stream/device/nwpi/upsertSetting
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def upsert_setting(self, payload: Optional[NwpiSettingDataPayload] = None, **kw):
        """
        insert or update setting

        :param payload: Payload
        :returns: None
        """
        logging.warning("Operation: %s is deprecated", "upsertSetting")
        return self._request_adapter.request(
            "POST", "/dataservice/stream/device/nwpi/upsertSetting", payload=payload, **kw
        )
