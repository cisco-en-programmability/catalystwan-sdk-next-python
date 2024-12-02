# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface
import logging
from .models import EdgeTypeParam


class EdgeBuilder:
    """
    Builds and executes requests for operations under /multicloud/connectivity/edge
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_edge_connectivity_details(
        self,
        edge_type: Optional[EdgeTypeParam] = None,
        connectivity_name: Optional[str] = None,
        connectivity_type: Optional[str] = None,
        edge_gateway_name: Optional[str] = None,
        **kw,
    ) -> Any:
        """
        Get Interconnect Connectivity details

        :param edge_type: Edge type
        :param connectivity_name: Connectivity Name
        :param connectivity_type: Connectivity Type
        :param edge_gateway_name: Interconnect Gateway name
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "getEdgeConnectivityDetails")
        params = {
            "edgeType": edge_type,
            "connectivityName": connectivity_name,
            "connectivityType": connectivity_type,
            "edgeGatewayName": edge_gateway_name,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/multicloud/connectivity/edge", params=params, **kw
        )

    @property
    def update_edge_connectivity(self):
        class update_edge_connectivity_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Update Interconnect connectivity

                :param payload: Edge connectivity
                :returns: Any
                """
                logging.warning("Operation: %s is deprecated", "updateEdgeConnectivity")
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/multicloud/connectivity/edge",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return update_edge_connectivity_(self._request_adapter)

    @property
    def create_edge_connectivity(self):
        class create_edge_connectivity_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Create Interconnect connectivity

                :param payload: Edge connectivity
                :returns: Any
                """
                logging.warning("Operation: %s is deprecated", "createEdgeConnectivity")
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/multicloud/connectivity/edge",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return create_edge_connectivity_(self._request_adapter)

    def delete_edge_connectivity(
        self, connection_name: str, delete_cloud_resources: Optional[str] = None, **kw
    ) -> Any:
        """
        Delete Interconnect connectivity

        :param connection_name: Edge connectivity name
        :param delete_cloud_resources: Delete Cloud Resources
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "deleteEdgeConnectivity")
        params = {
            "connectionName": connection_name,
            "deleteCloudResources": delete_cloud_resources,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/multicloud/connectivity/edge/{connectionName}",
            params=params,
            **kw,
        )

    def get_edge_connectivity_detail_by_name(self, connectivity_name: str, **kw) -> Any:
        """
        Get Interconnect Connectivity by name

        :param connectivity_name: IC-GW connectivity name
        :returns: Any
        """
        logging.warning(
            "Operation: %s is deprecated", "getEdgeConnectivityDetailByName"
        )
        params = {
            "connectivityName": connectivity_name,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/connectivity/edge/{connectivityName}",
            params=params,
            **kw,
        )
