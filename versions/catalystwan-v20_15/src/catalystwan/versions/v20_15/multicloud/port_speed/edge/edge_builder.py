# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any
from catalystwan.abc import RequestAdapterInterface
import logging
from .models import EdgeTypeParam
from .models import CloudTypeParam


class EdgeBuilder:
    """
    Builds and executes requests for operations under /multicloud/portSpeed/edge
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_port_speed(
        self,
        edge_type: EdgeTypeParam,
        edge_account_id: str,
        connectivity_type: str,
        cloud_type: Optional[CloudTypeParam] = None,
        cloud_account_id: Optional[str] = None,
        connect_type: Optional[str] = None,
        connect_sub_type: Optional[str] = None,
        connectivity_gateway: Optional[str] = None,
        partner_port: Optional[str] = None,
        **kw,
    ) -> Any:
        """
        Get supported port speed

        :param edge_type: Interconnect Provider
        :param edge_account_id: Interconnect Provider Account ID
        :param connectivity_type: Interconnect Connectivity Type
        :param cloud_type: Cloud Service Provider
        :param cloud_account_id: Cloud Service Provider Account ID
        :param connect_type: Connection Type filter
        :param connect_sub_type: Connection Sub-Type filter
        :param connectivity_gateway: Connectivity Gateway
        :param partner_port: partnerPort
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "getPortSpeed")
        params = {
            "edgeType": edge_type,
            "edgeAccountId": edge_account_id,
            "connectivityType": connectivity_type,
            "cloudType": cloud_type,
            "cloudAccountId": cloud_account_id,
            "connectType": connect_type,
            "connectSubType": connect_sub_type,
            "connectivityGateway": connectivity_gateway,
            "partnerPort": partner_port,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/portSpeed/edge/{edgeType}/{edgeAccountId}/{connectivityType}",
            params=params,
            **kw,
        )
