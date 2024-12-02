# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface
from .models import Aaa


class AaaBuilder:
    """
    Builds and executes requests for operations under /admin/aaa
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_aaa_config(self, **kw) -> Aaa:
        """
        Get aaa configuration


        Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

        :returns: Aaa
        """
        return self._request_adapter.request(
            "GET", "/dataservice/admin/aaa", return_type=Aaa, **kw
        )

    @property
    def update_aaa_config(self):
        class update_aaa_config_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Aaa] = None, **kw):
                """
                Update aaa configuration


                Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

                :param payload: aaa
                :returns: None
                """
                return self._request_adapter.request(
                    "PUT", "/dataservice/admin/aaa", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Aaa:
                return Aaa(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Aaa]:
                return Aaa

        return update_aaa_config_(self._request_adapter)

    @property
    def create_aaa_config(self):
        class create_aaa_config_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Aaa] = None, **kw):
                """
                Create aaa configuration


                Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

                :param payload: aaa
                :returns: None
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/admin/aaa", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Aaa:
                return Aaa(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Aaa]:
                return Aaa

        return create_aaa_config_(self._request_adapter)

    def delete_aaa_config(self, **kw):
        """
        Delete aaa configuration


        Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

        :returns: None
        """
        return self._request_adapter.request("DELETE", "/dataservice/admin/aaa", **kw)
