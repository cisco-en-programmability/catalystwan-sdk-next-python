# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from .models import InvalidateVmanageRootCa


class VmanagerootcaBuilder:
    """
    Builds and executes requests for operations under /system/device/vmanagerootca
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def invalidate_vmanage_root_ca(self, uuid: str, **kw) -> InvalidateVmanageRootCa:
        """
        Invalidate vManage root CA

        :param uuid: Device UUID
        :returns: InvalidateVmanageRootCa
        """
        params = {
            "uuid": uuid,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/system/device/vmanagerootca/{uuid}",
            return_type=InvalidateVmanageRootCa,
            params=params,
            **kw,
        )
