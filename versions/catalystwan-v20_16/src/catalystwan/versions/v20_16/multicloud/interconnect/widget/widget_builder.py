# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import List

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import InterconnectWidget


class WidgetBuilder:
    """
    Builds and executes requests for operations under /multicloud/interconnect/widget
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_all_interconnect_widgets(self, **kw) -> List[InterconnectWidget]:
        """
        API to retrieve all Interconnect widgets.

        :returns: List[InterconnectWidget]
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/interconnect/widget",
            return_type=List[InterconnectWidget],
            **kw,
        )

    def get_interconnect_widget(self, interconnect_type: str, **kw) -> InterconnectWidget:
        """
        API to retrieve an Interconnect widget for an Interconnect type.

        :param interconnect_type: Interconnect provider type
        :returns: InterconnectWidget
        """
        params = {
            "interconnect-type": interconnect_type,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/interconnect/{interconnect-type}/widget",
            return_type=InterconnectWidget,
            params=params,
            **kw,
        )
