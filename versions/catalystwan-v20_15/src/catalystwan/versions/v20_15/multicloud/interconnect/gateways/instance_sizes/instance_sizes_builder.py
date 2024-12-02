# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from catalystwan.abc import RequestAdapterInterface
from .models import InlineResponse2004
from .models import InterconnectTypeParam


class InstanceSizesBuilder:
    """
    Builds and executes requests for operations under /multicloud/interconnect/gateways/instance-sizes
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_interconnect_gateway_instance_sizes(
        self, interconnect_type: InterconnectTypeParam, **kw
    ) -> InlineResponse2004:
        """
        API to retrieve Interconnect Gateway instance sizes supported by an  Interconnect provider.

        :param interconnect_type: Interconnect provider type
        :returns: InlineResponse2004
        """
        params = {
            "interconnect-type": interconnect_type,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/interconnect/gateways/instance-sizes",
            return_type=InlineResponse2004,
            params=params,
            **kw,
        )
