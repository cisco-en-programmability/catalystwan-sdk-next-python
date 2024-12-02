# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class AttachcliBuilder:
    """
    Builds and executes requests for operations under /template/device/config/attachcli
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def push_cli_template(self):
        class push_cli_template_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Attach CLI device template


                Note: In a multitenant vManage system, this API is only available in the Provider view.

                :param payload: Device template
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/template/device/config/attachcli",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return push_cli_template_(self._request_adapter)
