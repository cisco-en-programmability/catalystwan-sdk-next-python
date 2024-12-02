# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import List, Any
from catalystwan.abc import RequestAdapterInterface


class DevicesBuilder:
    """
    Builds and executes requests for operations under /mdp/devices
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def retrieve_mdp_supported_devices_(self, nms_id: str, **kw) -> List[Any]:
        """
        Retrieve MDP supported devices

        :param nms_id: Nms id
        :returns: List[Any]
        """
        params = {
            "nmsId": nms_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/mdp/devices/{nmsId}",
            return_type=List[Any],
            params=params,
            **kw,
        )
