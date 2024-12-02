# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import DeployTopologyGroupPostRequest


class DeployBuilder:
    """
    Builds and executes requests for operations under /v1/topology-group/{topologyGroupId}/device/deploy
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def deploy_topology_group(self):
        class deploy_topology_group_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                topology_group_id: str,
                payload: Optional[DeployTopologyGroupPostRequest] = None,
                **kw,
            ) -> str:
                """
                deploy Topology group to devices

                :param topology_group_id: Topology Group Id
                :param payload: Payload
                :returns: str
                """
                params = {
                    "topologyGroupId": topology_group_id,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/topology-group/{topologyGroupId}/device/deploy",
                    return_type=str,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> DeployTopologyGroupPostRequest:
                return DeployTopologyGroupPostRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[DeployTopologyGroupPostRequest]:
                return DeployTopologyGroupPostRequest

        return deploy_topology_group_(self._request_adapter)
