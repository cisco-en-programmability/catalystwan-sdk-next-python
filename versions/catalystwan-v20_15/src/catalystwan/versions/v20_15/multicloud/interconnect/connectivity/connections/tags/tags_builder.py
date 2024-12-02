# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from .models import InlineResponse2002


class TagsBuilder:
    """
    Builds and executes requests for operations under /multicloud/interconnect/connectivity/connections/tags
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_interconnect_mapping_tags(
        self,
        cloud_type: str,
        cloud_account_id: str,
        resource_group: Optional[str] = None,
        **kw,
    ) -> InlineResponse2002:
        """
        API to retrieve configured Interconnect host VPC/VNET mapping tags.

        :param cloud_type: Cloud provider type
        :param cloud_account_id: Cloud account id
        :param resource_group: Azure cloud resource group name
        :returns: InlineResponse2002
        """
        params = {
            "cloud-type": cloud_type,
            "cloud-account-id": cloud_account_id,
            "resource-group": resource_group,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/interconnect/connectivity/connections/tags",
            return_type=InlineResponse2002,
            params=params,
            **kw,
        )
