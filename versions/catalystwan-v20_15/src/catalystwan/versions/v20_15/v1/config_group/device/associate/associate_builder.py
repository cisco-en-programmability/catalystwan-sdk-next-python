# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class AssociateBuilder:
    """
    Builds and executes requests for operations under /v1/config-group/{configGroupId}/device/associate
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_config_group_association(self, config_group_id: str, **kw):
        """
        Get devices association with a config group

        :param config_group_id: Config group id
        :returns: None
        """
        params = {
            "configGroupId": config_group_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/config-group/{configGroupId}/device/associate",
            params=params,
            **kw,
        )

    @property
    def update_config_group_association(self):
        class update_config_group_association_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, config_group_id: str, payload: Optional[Any] = None, **kw
            ):
                """
                Move the devices from one config group to another

                :param config_group_id: Config group id
                :param payload: Payload
                :returns: None
                """
                params = {
                    "configGroupId": config_group_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/config-group/{configGroupId}/device/associate",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return update_config_group_association_(self._request_adapter)

    @property
    def create_config_group_association(self):
        class create_config_group_association_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, config_group_id: str, payload: Optional[Any] = None, **kw
            ):
                """
                Create associations with device and a config group

                :param config_group_id: Config group id
                :param payload: Payload
                :returns: None
                """
                params = {
                    "configGroupId": config_group_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/config-group/{configGroupId}/device/associate",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return create_config_group_association_(self._request_adapter)

    @property
    def delete_config_group_association(self):
        class delete_config_group_association_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, config_group_id: str, payload: Optional[Any] = None, **kw
            ):
                """
                Delete Config Group Association from devices

                :param config_group_id: Config group id
                :param payload: Payload
                :returns: None
                """
                params = {
                    "configGroupId": config_group_id,
                }
                return self._request_adapter.request(
                    "DELETE",
                    "/dataservice/v1/config-group/{configGroupId}/device/associate",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return delete_config_group_association_(self._request_adapter)
