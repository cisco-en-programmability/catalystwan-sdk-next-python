# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import List
from catalystwan.abc import RequestAdapterInterface
from .models import VnicInfo


class VnicsInfoBuilder:
    """
    Builds and executes requests for operations under /stream/device/capture/vnicsInfo
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_vnic_info_by_vnf_id(self, vnf_id: str, **kw) -> List[VnicInfo]:
        """
        Get vnic info by vrfId

        :param vnf_id: Vnf id
        :returns: List[VnicInfo]
        """
        params = {
            "vnfId": vnf_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/stream/device/capture/vnicsInfo/{vnfId}",
            return_type=List[VnicInfo],
            params=params,
            **kw,
        )
