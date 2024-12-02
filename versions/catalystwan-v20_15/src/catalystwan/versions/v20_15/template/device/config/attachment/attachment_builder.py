# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type
from catalystwan.abc import RequestAdapterInterface


class AttachmentBuilder:
    """
    Builds and executes requests for operations under /template/device/config/attachment
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def attach_device_template(self):
        class attach_device_template_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Attach device template


                Note: In a multitenant vManage system, this API is only available in the Provider view.

                :param payload: Device template
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/template/device/config/attachment",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return attach_device_template_(self._request_adapter)
