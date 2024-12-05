# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import CreateConfigGroupDeviceVariablesPutRequest

if TYPE_CHECKING:
    from .schema.schema_builder import SchemaBuilder


class VariablesBuilder:
    """
    Builds and executes requests for operations under /v1/config-group/{configGroupId}/device/variables
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_config_group_device_variables(
        self, config_group_id: str, device_id: Optional[str] = None, suggestions: Optional[bool] = None, **kw
    ) -> Any:
        """
        Get device variables

        :param config_group_id: Config Group Id
        :param device_id: Comma separated device id's like d1,d2
        :param suggestions: Suggestions for possible values
        :returns: Any
        """
        params = {
            "configGroupId": config_group_id,
            "device-id": device_id,
            "suggestions": suggestions,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/v1/config-group/{configGroupId}/device/variables", params=params, **kw
        )

    @property
    def create_config_group_device_variables(self):
        class create_config_group_device_variables_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, config_group_id: str, payload: Optional[CreateConfigGroupDeviceVariablesPutRequest] = None, **kw
            ) -> Any:
                """
                assign values to device variables

                :param config_group_id: Config Group Id
                :param payload: Payload
                :returns: Any
                """
                params = {
                    "configGroupId": config_group_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/config-group/{configGroupId}/device/variables",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> CreateConfigGroupDeviceVariablesPutRequest:
                return CreateConfigGroupDeviceVariablesPutRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[CreateConfigGroupDeviceVariablesPutRequest]:
                return CreateConfigGroupDeviceVariablesPutRequest

        return create_config_group_device_variables_(self._request_adapter)

    @property
    def fetch_config_group_device_variables(self):
        class fetch_config_group_device_variables_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, config_group_id: str, payload: Optional[CreateConfigGroupDeviceVariablesPutRequest] = None, **kw
            ) -> Any:
                """
                Fetch device variables

                :param config_group_id: Config Group Id
                :param payload: Payload
                :returns: Any
                """
                params = {
                    "configGroupId": config_group_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/config-group/{configGroupId}/device/variables",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> CreateConfigGroupDeviceVariablesPutRequest:
                return CreateConfigGroupDeviceVariablesPutRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[CreateConfigGroupDeviceVariablesPutRequest]:
                return CreateConfigGroupDeviceVariablesPutRequest

        return fetch_config_group_device_variables_(self._request_adapter)

    @property
    def schema(self) -> SchemaBuilder:
        """
        The schema property
        """
        from .schema.schema_builder import SchemaBuilder

        return SchemaBuilder(self._request_adapter)
