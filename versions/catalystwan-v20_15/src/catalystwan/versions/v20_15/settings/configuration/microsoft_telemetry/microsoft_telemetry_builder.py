# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class MicrosoftTelemetryBuilder:
    """
    Builds and executes requests for operations under /settings/configuration/microsoftTelemetry
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_microsoft_telemetry_configuration(self, **kw) -> Any:
        """
        Retrieve Microsoft telemetry configuration value

        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "getMicrosoftTelemetryConfiguration")
        return self._request_adapter.request(
            "GET", "/dataservice/settings/configuration/microsoftTelemetry", **kw
        )

    def edit_microsoft_telemetry_configuration(self, payload: Optional[str] = None, **kw) -> Any:
        """
        Update Microsoft telemetry configuration setting

        :param payload: Payload
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "editMicrosoftTelemetryConfiguration")
        return self._request_adapter.request(
            "PUT", "/dataservice/settings/configuration/microsoftTelemetry", payload=payload, **kw
        )

    def new_microsoft_telemetry_configuration(self, payload: Optional[str] = None, **kw) -> str:
        """
        Add new Microsoft telemetry configuration

        :param payload: Payload
        :returns: str
        """
        logging.warning("Operation: %s is deprecated", "newMicrosoftTelemetryConfiguration")
        return self._request_adapter.request(
            "POST",
            "/dataservice/settings/configuration/microsoftTelemetry",
            return_type=str,
            payload=payload,
            **kw,
        )
