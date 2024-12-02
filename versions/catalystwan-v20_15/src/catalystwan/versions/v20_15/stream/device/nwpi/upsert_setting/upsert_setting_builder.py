# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import NwpiSettingDataPayload


class UpsertSettingBuilder:
    """
    Builds and executes requests for operations under /stream/device/nwpi/upsertSetting
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def upsert_setting(self):
        class upsert_setting_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[NwpiSettingDataPayload] = None, **kw):
                """
                insert or update setting

                :param payload: Payload
                :returns: None
                """
                logging.warning("Operation: %s is deprecated", "upsertSetting")
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/stream/device/nwpi/upsertSetting",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> NwpiSettingDataPayload:
                return NwpiSettingDataPayload(*args, **kwargs)

            @property
            def payload_model(self) -> Type[NwpiSettingDataPayload]:
                return NwpiSettingDataPayload

        return upsert_setting_(self._request_adapter)
