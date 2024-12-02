# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class AttachmentBuilder:
    """
    Builds and executes requests for operations under /networkdesign/attachment
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def push_network_design(self):
        class push_network_design_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Attach network design

                :param payload: Device template
                :returns: Any
                """
                logging.warning("Operation: %s is deprecated", "pushNetworkDesign")
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/networkdesign/attachment",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return push_network_design_(self._request_adapter)
