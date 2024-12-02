# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface
from .models import DeployConfigGroupPostRequest


class DeployBuilder:
    """
    Builds and executes requests for operations under /v1/config-group/{configGroupId}/device/deploy
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def deploy_config_group(self):
        class deploy_config_group_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                config_group_id: str,
                payload: Optional[DeployConfigGroupPostRequest] = None,
                **kw,
            ) -> str:
                """
                deploy config group to devices


                Note: In a multitenant vManage system, this API is only available in the Provider view.

                :param config_group_id: Config Group Id
                :param payload: Payload
                :returns: str
                """
                params = {
                    "configGroupId": config_group_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/config-group/{configGroupId}/device/deploy",
                    return_type=str,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> DeployConfigGroupPostRequest:
                return DeployConfigGroupPostRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[DeployConfigGroupPostRequest]:
                return DeployConfigGroupPostRequest

        return deploy_config_group_(self._request_adapter)
