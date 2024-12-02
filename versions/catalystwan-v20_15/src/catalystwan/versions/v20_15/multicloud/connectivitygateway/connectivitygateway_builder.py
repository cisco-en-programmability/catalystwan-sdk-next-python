# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import EdgeTypeParam


class ConnectivitygatewayBuilder:
    """
    Builds and executes requests for operations under /multicloud/connectivitygateway
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_connectivity_gateways(
        self,
        account_id: Optional[str] = None,
        cloud_type: Optional[str] = None,
        connectivity_type: Optional[str] = None,
        connectivity_gateway_name: Optional[str] = None,
        region: Optional[str] = None,
        network: Optional[str] = None,
        state: Optional[str] = None,
        refresh: Optional[str] = None,
        edge_type: Optional[EdgeTypeParam] = None,
        **kw,
    ) -> Any:
        """
        Get all Connectivity Gateways

        :param account_id: Account Id
        :param cloud_type: Cloud Type
        :param connectivity_type: Cloud Connectivity Type
        :param connectivity_gateway_name: Connectivity Gateway Name
        :param region: Region
        :param network: Network
        :param state: State
        :param refresh: Refresh
        :param edge_type: Edge type
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "getConnectivityGateways")
        params = {
            "accountId": account_id,
            "cloudType": cloud_type,
            "connectivityType": connectivity_type,
            "connectivityGatewayName": connectivity_gateway_name,
            "region": region,
            "network": network,
            "state": state,
            "refresh": refresh,
            "edgeType": edge_type,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/multicloud/connectivitygateway", params=params, **kw
        )

    @property
    def create_connectivity_gateway(self):
        class create_connectivity_gateway_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Create Connectivity gateway

                :param payload: Connectivity gateway
                :returns: Any
                """
                logging.warning(
                    "Operation: %s is deprecated", "createConnectivityGateway"
                )
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/multicloud/connectivitygateway",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return create_connectivity_gateway_(self._request_adapter)

    def clean_up_all_connectivity_gateways_in_local_db(
        self, deletion_type: Optional[str] = None, **kw
    ) -> Any:
        """
        Delete all Connectivity Gateways in local DB

        :param deletion_type: Deletion Type
        :returns: Any
        """
        logging.warning(
            "Operation: %s is deprecated", "cleanUpAllConnectivityGatewaysInLocalDB"
        )
        params = {
            "deletionType": deletion_type,
        }
        return self._request_adapter.request(
            "DELETE", "/dataservice/multicloud/connectivitygateway", params=params, **kw
        )

    def delete_connectivity_gateway(
        self,
        cloud_provider: str,
        connectivity_gateway_name: str,
        connectivity_type: Optional[str] = None,
        **kw,
    ) -> Any:
        """
        Delete Connectivity Gateway

        :param cloud_provider: Cloud Provider
        :param connectivity_gateway_name: Connectivity gateway name
        :param connectivity_type: Cloud Connectivity Type
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "deleteConnectivityGateway")
        params = {
            "cloudProvider": cloud_provider,
            "connectivityGatewayName": connectivity_gateway_name,
            "connectivityType": connectivity_type,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/multicloud/connectivitygateway/{cloudProvider}/{connectivityGatewayName}",
            params=params,
            **kw,
        )
