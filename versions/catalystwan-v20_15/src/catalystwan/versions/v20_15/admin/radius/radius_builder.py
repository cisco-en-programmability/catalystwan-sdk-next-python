# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import Radius


class RadiusBuilder:
    """
    Builds and executes requests for operations under /admin/radius
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_radius_config(self, **kw) -> Radius:
        """
        Get radius configuration


        Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

        :returns: Radius
        """
        return self._request_adapter.request("GET", "/dataservice/admin/radius", return_type=Radius, **kw)

    @property
    def update_radius_config(self):
        class update_radius_config_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Radius] = None, **kw):
                """
                Update radius configuration


                Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

                :param payload: radius
                :returns: None
                """
                return self._request_adapter.request("PUT", "/dataservice/admin/radius", payload=payload, **kw)

            def create_payload(self, *args, **kwargs) -> Radius:
                return Radius(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Radius]:
                return Radius

        return update_radius_config_(self._request_adapter)

    @property
    def create_radius_config(self):
        class create_radius_config_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Radius] = None, **kw):
                """
                Create radius configuration


                Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

                :param payload: radius
                :returns: None
                """
                return self._request_adapter.request("POST", "/dataservice/admin/radius", payload=payload, **kw)

            def create_payload(self, *args, **kwargs) -> Radius:
                return Radius(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Radius]:
                return Radius

        return create_radius_config_(self._request_adapter)

    def delete_radius_config(self, **kw) -> Radius:
        """
        Delete radius configuration


        Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

        :returns: Radius
        """
        return self._request_adapter.request("DELETE", "/dataservice/admin/radius", return_type=Radius, **kw)
