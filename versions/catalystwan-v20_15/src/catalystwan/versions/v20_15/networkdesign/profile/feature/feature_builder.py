# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import List, Any
from catalystwan.abc import RequestAdapterInterface
import logging


class FeatureBuilder:
    """
    Builds and executes requests for operations under /networkdesign/profile/feature
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_device_profile_feature_template_list(self, **kw) -> List[Any]:
        """
        Generate device profile template list

        :returns: List[Any]
        """
        logging.warning(
            "Operation: %s is deprecated", "getDeviceProfileFeatureTemplateList"
        )
        return self._request_adapter.request(
            "GET",
            "/dataservice/networkdesign/profile/feature",
            return_type=List[Any],
            **kw,
        )
