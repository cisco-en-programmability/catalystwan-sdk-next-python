# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import List, Any
from catalystwan.abc import RequestAdapterInterface


class DevicesWithoutSubjectSudiBuilder:
    """
    Builds and executes requests for operations under /system/device/devicesWithoutSubjectSudi
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def devices_without_subject_sudi(self, **kw) -> List[Any]:
        """
        retrieve devices without subject sudi

        :returns: List[Any]
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/system/device/devicesWithoutSubjectSudi",
            return_type=List[Any],
            **kw,
        )
