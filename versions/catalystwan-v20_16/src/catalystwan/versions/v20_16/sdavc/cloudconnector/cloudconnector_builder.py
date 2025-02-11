# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import DisableCloudConnectorPutRequest

if TYPE_CHECKING:
    from .status.status_builder import StatusBuilder


class CloudconnectorBuilder:
    """
    Builds and executes requests for operations under /sdavc/cloudconnector
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_cloud_connector(self, **kw) -> Any:
        """
        Get SD_AVC Cloud Connector Config

        :returns: Any
        """
        return self._request_adapter.request("GET", "/dataservice/sdavc/cloudconnector", **kw)

    def disable_cloud_connector(
        self, payload: Optional[DisableCloudConnectorPutRequest] = None, **kw
    ) -> Any:
        """
        Disable SD_AVC Cloud Connector

        :param payload: Payload
        :returns: Any
        """
        return self._request_adapter.request(
            "PUT", "/dataservice/sdavc/cloudconnector", payload=payload, **kw
        )

    def enable_cloud_connector(
        self, payload: Optional[DisableCloudConnectorPutRequest] = None, **kw
    ) -> Any:
        """
        Enable SD_AVC Cloud Connector

        :param payload: Payload
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/sdavc/cloudconnector", payload=payload, **kw
        )

    @property
    def status(self) -> StatusBuilder:
        """
        The status property
        """
        from .status.status_builder import StatusBuilder

        return StatusBuilder(self._request_adapter)
