# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import List

from catalystwan.abc import RequestAdapterInterface

from .models import CloudTypeParam, MapDefaults


class DefaultsBuilder:
    """
    Builds and executes requests for operations under /multicloud/map/defaults
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_default_mapping_values(self, cloud_type: CloudTypeParam, **kw) -> List[MapDefaults]:
        """
        Get default mapping values

        :param cloud_type: Cloud type
        :returns: List[MapDefaults]
        """
        params = {
            "cloudType": cloud_type,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/multicloud/map/defaults", return_type=List[MapDefaults], params=params, **kw
        )
