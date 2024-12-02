# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type
from catalystwan.abc import RequestAdapterInterface
from .models import Tacacs


class TacacsBuilder:
    """
    Builds and executes requests for operations under /admin/tacacs
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_tacacs_config(self, **kw) -> Tacacs:
        """
        Get tacacs configuration


        Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

        :returns: Tacacs
        """
        return self._request_adapter.request(
            "GET", "/dataservice/admin/tacacs", return_type=Tacacs, **kw
        )

    @property
    def update_tacacs_config(self):
        class update_tacacs_config_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Tacacs] = None, **kw):
                """
                Update tacacs configuration


                Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

                :param payload: tacacs
                :returns: None
                """
                return self._request_adapter.request(
                    "PUT", "/dataservice/admin/tacacs", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Tacacs:
                return Tacacs(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Tacacs]:
                return Tacacs

        return update_tacacs_config_(self._request_adapter)

    @property
    def create_tacacs_config(self):
        class create_tacacs_config_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Tacacs] = None, **kw):
                """
                Create tacacs configuration


                Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

                :param payload: tacacs
                :returns: None
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/admin/tacacs", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Tacacs:
                return Tacacs(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Tacacs]:
                return Tacacs

        return create_tacacs_config_(self._request_adapter)

    def delete_tacacs_config(self, **kw) -> Tacacs:
        """
        Delete tacacs configuration


        Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

        :returns: Tacacs
        """
        return self._request_adapter.request(
            "DELETE", "/dataservice/admin/tacacs", return_type=Tacacs, **kw
        )
