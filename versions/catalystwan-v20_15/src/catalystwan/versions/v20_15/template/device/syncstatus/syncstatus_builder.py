# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import List, Any
from catalystwan.abc import RequestAdapterInterface


class SyncstatusBuilder:
    """
    Builds and executes requests for operations under /template/device/syncstatus
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_out_of_sync_templates(self, **kw) -> List[Any]:
        """
        Get template sync status


        Note: In a multitenant vManage system, this API is only available in the Provider view.

        :returns: List[Any]
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/template/device/syncstatus",
            return_type=List[Any],
            **kw,
        )

    def get_out_of_sync_devices(self, template_id: str, **kw) -> List[Any]:
        """
        Get out of sync devices


        Note: In a multitenant vManage system, this API is only available in the Provider view.

        :param template_id: Template Id
        :returns: List[Any]
        """
        params = {
            "templateId": template_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/template/device/syncstatus/{templateId}",
            return_type=List[Any],
            params=params,
            **kw,
        )
