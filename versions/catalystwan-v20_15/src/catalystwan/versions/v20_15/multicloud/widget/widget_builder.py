# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, List

from catalystwan.abc import RequestAdapterInterface

from .models import CloudWidget

if TYPE_CHECKING:
    from .edge.edge_builder import EdgeBuilder


class WidgetBuilder:
    """
    Builds and executes requests for operations under /multicloud/widget
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_all_cloud_widgets(self, **kw) -> List[CloudWidget]:
        """
        Get All cloud widgets

        :returns: List[CloudWidget]
        """
        return self._request_adapter.request(
            "GET", "/dataservice/multicloud/widget", return_type=List[CloudWidget], **kw
        )

    def get_cloud_widget(self, cloud_type: str, **kw) -> CloudWidget:
        """
        Get cloud widget by cloud type

        :param cloud_type: Cloud type
        :returns: CloudWidget
        """
        params = {
            "cloudType": cloud_type,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/multicloud/widget/{cloudType}", return_type=CloudWidget, params=params, **kw
        )

    @property
    def edge(self) -> EdgeBuilder:
        """
        The edge property
        """
        from .edge.edge_builder import EdgeBuilder

        return EdgeBuilder(self._request_adapter)
