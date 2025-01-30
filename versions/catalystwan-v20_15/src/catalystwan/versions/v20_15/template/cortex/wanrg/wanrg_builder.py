# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class WanrgBuilder:
    """
    Builds and executes requests for operations under /template/cortex/wanrg
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_wan_resource_groups(self, accountid: str, **kw) -> Any:
        """
        Get WAN Resource Groups

        :param accountid: Account Id
        :returns: Any
        """
        params = {
            "accountid": accountid,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/template/cortex/wanrg", params=params, **kw
        )

    def edit_wan_resource_groups(self, payload: Optional[Any] = None, **kw):
        """
        Edit WAN Resource Groups

        :param payload: WAN resource group
        :returns: None
        """
        return self._request_adapter.request(
            "PUT", "/dataservice/template/cortex/wanrg", payload=payload, **kw
        )

    def save_wan_resource_groups(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Create WAN Resource Groups

        :param payload: WAN resource group
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/template/cortex/wanrg", payload=payload, **kw
        )

    def delete_wan_resource_groups(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Delete WAN Resource Groups

        :param payload: WAN resource group
        :returns: Any
        """
        return self._request_adapter.request(
            "DELETE", "/dataservice/template/cortex/wanrg", payload=payload, **kw
        )
