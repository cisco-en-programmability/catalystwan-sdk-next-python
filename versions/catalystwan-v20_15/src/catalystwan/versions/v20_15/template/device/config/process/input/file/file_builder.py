# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class FileBuilder:
    """
    Builds and executes requests for operations under /template/device/config/process/input/file
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def process_input_comma_sep_file(self):
        class process_input_comma_sep_file_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> str:
                """
                Process input comma separated file


                Note: In a multitenant vManage system, this API is only available in the Provider view.

                :param payload: Device template
                :returns: str
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/template/device/config/process/input/file",
                    return_type=str,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return process_input_comma_sep_file_(self._request_adapter)
