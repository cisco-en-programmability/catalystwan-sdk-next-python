# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import Aaa


class AaaBuilder:
    """
    Builds and executes requests for operations under /admin/aaa
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_aaa_config(self, **kw) -> Aaa:
        """
        Get aaa configuration


        Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

        :returns: Aaa
        """
        return self._request_adapter.request("GET", "/dataservice/admin/aaa", return_type=Aaa, **kw)

    def update_aaa_config(self, payload: Optional[Aaa] = None, **kw):
        """
        Update aaa configuration


        Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

        :param payload: aaa
        :returns: None
        """
        return self._request_adapter.request("PUT", "/dataservice/admin/aaa", payload=payload, **kw)

    def create_aaa_config(self, payload: Optional[Aaa] = None, **kw):
        """
        Create aaa configuration


        Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

        :param payload: aaa
        :returns: None
        """
        return self._request_adapter.request(
            "POST", "/dataservice/admin/aaa", payload=payload, **kw
        )

    def delete_aaa_config(self, **kw):
        """
        Delete aaa configuration


        Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

        :returns: None
        """
        return self._request_adapter.request("DELETE", "/dataservice/admin/aaa", **kw)
