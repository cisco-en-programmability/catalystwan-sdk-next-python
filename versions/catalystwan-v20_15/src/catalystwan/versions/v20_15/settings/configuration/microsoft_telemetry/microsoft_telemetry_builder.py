# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface
import logging


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
        logging.warning(
            "Operation: %s is deprecated", "getMicrosoftTelemetryConfiguration"
        )
        return self._request_adapter.request(
            "GET", "/dataservice/settings/configuration/microsoftTelemetry", **kw
        )

    @property
    def edit_microsoft_telemetry_configuration(self):
        class edit_microsoft_telemetry_configuration_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[str] = None, **kw) -> Any:
                """
                Update Microsoft telemetry configuration setting

                :param payload: Payload
                :returns: Any
                """
                logging.warning(
                    "Operation: %s is deprecated", "editMicrosoftTelemetryConfiguration"
                )
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/settings/configuration/microsoftTelemetry",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return edit_microsoft_telemetry_configuration_(self._request_adapter)

    @property
    def new_microsoft_telemetry_configuration(self):
        class new_microsoft_telemetry_configuration_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[str] = None, **kw) -> str:
                """
                Add new Microsoft telemetry configuration

                :param payload: Payload
                :returns: str
                """
                logging.warning(
                    "Operation: %s is deprecated", "newMicrosoftTelemetryConfiguration"
                )
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/settings/configuration/microsoftTelemetry",
                    return_type=str,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return new_microsoft_telemetry_configuration_(self._request_adapter)
