# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from catalystwan.abc import RequestAdapterInterface

from .models import ProcessResponse

if TYPE_CHECKING:
    from .tags.tags_builder import TagsBuilder


class ConnectionsBuilder:
    """
    Builds and executes requests for operations under /multicloud/interconnect/connectivity/connections
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_interconnect_connectivitys(
        self,
        interconnect_type: Optional[str] = None,
        interconnect_gateway_name: Optional[str] = None,
        connection_name: Optional[str] = None,
        connection_type: Optional[str] = None,
        refresh: Optional[str] = "false",
        **kw,
    ) -> Any:
        """
        API to retrieve all exisiting Interconnect connectivity.

        :param interconnect_type: Interconnect provider Type
        :param interconnect_gateway_name: Interconnect gateway name
        :param connection_name: Interconnect connectivity name
        :param connection_type: Interconnect connectivity type
        :param refresh: Interconnect connection provider sync enabled
        :returns: Any
        """
        params = {
            "interconnect-type": interconnect_type,
            "interconnect-gateway-name": interconnect_gateway_name,
            "connection-name": connection_name,
            "connection-type": connection_type,
            "refresh": refresh,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/multicloud/interconnect/connectivity/connections", params=params, **kw
        )

    def create_interconnect_connectivity(self, payload: Optional[Any] = None, **kw) -> ProcessResponse:
        """
        API to create a private transit or cloud connection on an Interconnect Gateway at an Interconnect Provider.

        :param payload: Request Payload for Multicloud Interconnect Connections
        :returns: ProcessResponse
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/multicloud/interconnect/connectivity/connections",
            return_type=ProcessResponse,
            payload=payload,
            **kw,
        )

    def get_interconnect_connectivity(self, connection_name: str, **kw) -> Any:
        """
        API to retrieve an exisiting Interconnect connectivity.

        :param connection_name: Interconnect connectivity name
        :returns: Any
        """
        params = {
            "connection-name": connection_name,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/interconnect/connectivity/connections/{connection-name}",
            params=params,
            **kw,
        )

    def update_interconnect_connectivity(self, connection_name: str, payload: Optional[Any] = None, **kw) -> Any:
        """
        API to update an Interconnect connectivity at an Interconnect provider.

        :param connection_name: Interconnect connectivity name
        :param payload: Request Payload for Multicloud Interconnect Connections
        :returns: Any
        """
        params = {
            "connection-name": connection_name,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/multicloud/interconnect/connectivity/connections/{connection-name}",
            params=params,
            payload=payload,
            **kw,
        )

    def delete_interconnect_connectivity(
        self, connection_name: str, delete_cloud_resources: Optional[str] = "false", **kw
    ) -> ProcessResponse:
        """
        API to delete an Interconnect connectivity at an Interconnect provider.

        :param connection_name: Interconnect connectivity name
        :param delete_cloud_resources: Delete Interconnect conenction related cloud resorces enabled
        :returns: ProcessResponse
        """
        params = {
            "connection-name": connection_name,
            "delete-cloud-resources": delete_cloud_resources,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/multicloud/interconnect/connectivity/connections/{connection-name}",
            return_type=ProcessResponse,
            params=params,
            **kw,
        )

    @property
    def tags(self) -> TagsBuilder:
        """
        The tags property
        """
        from .tags.tags_builder import TagsBuilder

        return TagsBuilder(self._request_adapter)
