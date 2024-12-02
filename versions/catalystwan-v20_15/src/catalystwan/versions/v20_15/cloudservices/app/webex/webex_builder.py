# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class WebexBuilder:
    """
    Builds and executes requests for operations under /cloudservices/app/webex
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def enable_webex_1(self):
        class enable_webex_1_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> List[Any]:
                """
                Day N- Update Webex App

                :param payload: Cloudx apps and vpns
                :returns: List[Any]
                """
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/cloudservices/app/webex",
                    return_type=List[Any],
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return enable_webex_1_(self._request_adapter)

    @property
    def enable_webex(self):
        class enable_webex_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> List[Any]:
                """
                Add Webex App

                :param payload: Cloudx apps and vpns
                :returns: List[Any]
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/cloudservices/app/webex",
                    return_type=List[Any],
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return enable_webex_(self._request_adapter)

    @property
    def delete_webex_prefix_lists(self):
        class delete_webex_prefix_lists_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> List[Any]:
                """
                deleteWebexPrefixLists

                :param payload: TMP-Cloudx apps and vpns
                :returns: List[Any]
                """
                return self._request_adapter.request(
                    "DELETE",
                    "/dataservice/cloudservices/app/webex",
                    return_type=List[Any],
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return delete_webex_prefix_lists_(self._request_adapter)
