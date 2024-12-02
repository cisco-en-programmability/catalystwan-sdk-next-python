# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface
from .models import TopologyGroup

if TYPE_CHECKING:
    from .device.device_builder import DeviceBuilder


class TopologyGroupBuilder:
    """
    Builds and executes requests for operations under /v1/topology-group
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_topology_group_by_solution(
        self, solution: Optional[str] = None, **kw
    ) -> List[TopologyGroup]:
        """
        Get a Topology Group by Solution

        :param solution: Solution
        :returns: List[TopologyGroup]
        """
        params = {
            "solution": solution,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/topology-group",
            return_type=List[TopologyGroup],
            params=params,
            **kw,
        )

    @property
    def create_topology_group(self):
        class create_topology_group_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[str] = None, **kw) -> str:
                """
                Create a new Topology Group

                :param payload: Topology Group
                :returns: str
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/topology-group",
                    return_type=str,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return create_topology_group_(self._request_adapter)

    def get_topology_group(self, topology_group_id: str, **kw) -> TopologyGroup:
        """
        Get a Topology Group by ID

        :param topology_group_id: Topology group id
        :returns: TopologyGroup
        """
        params = {
            "topologyGroupId": topology_group_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/topology-group/{topologyGroupId}",
            return_type=TopologyGroup,
            params=params,
            **kw,
        )

    @property
    def edit_topology_group(self):
        class edit_topology_group_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, topology_group_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Edit a Topology Group

                :param topology_group_id: Topology group id
                :param payload: Topology Group
                :returns: str
                """
                params = {
                    "topologyGroupId": topology_group_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/topology-group/{topologyGroupId}",
                    return_type=str,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return edit_topology_group_(self._request_adapter)

    def delete_topology_group(self, topology_group_id: str, **kw):
        """
        Delete Topology Group

        :param topology_group_id: Topology group id
        :returns: None
        """
        params = {
            "topologyGroupId": topology_group_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/topology-group/{topologyGroupId}",
            params=params,
            **kw,
        )

    @property
    def device(self) -> DeviceBuilder:
        """
        The device property
        """
        from .device.device_builder import DeviceBuilder

        return DeviceBuilder(self._request_adapter)
