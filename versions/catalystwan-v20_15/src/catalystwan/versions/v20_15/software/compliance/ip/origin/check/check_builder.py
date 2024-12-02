# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List, Any, Type
from catalystwan.abc import RequestAdapterInterface


class CheckBuilder:
    """
    Builds and executes requests for operations under /software/compliance/ip/origin/check
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def check_given_ip_list(self):
        class check_given_ip_list_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> List[Any]:
                """
                Block IP based on list

                :param payload: Device detail
                :returns: List[Any]
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/software/compliance/ip/origin/check",
                    return_type=List[Any],
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return check_given_ip_list_(self._request_adapter)
