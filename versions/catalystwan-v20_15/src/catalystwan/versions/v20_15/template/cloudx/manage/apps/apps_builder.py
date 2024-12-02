# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional, Type

from catalystwan.abc import RequestAdapterInterface


class AppsBuilder:
    """
    Builds and executes requests for operations under /template/cloudx/manage/apps
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_apps(self, **kw) -> List[Any]:
        """
        Get apps and vpns

        :returns: List[Any]
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/template/cloudx/manage/apps",
            return_type=List[Any],
            **kw,
        )

    @property
    def edit_apps(self):
        class edit_apps_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Edit apps and vpns

                :param payload: Cloudx apps and vpns
                :returns: Any
                """
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/template/cloudx/manage/apps",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return edit_apps_(self._request_adapter)

    @property
    def add_apps(self):
        class add_apps_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> List[Any]:
                """
                Add apps and vpns

                :param payload: Cloudx apps and vpns
                :returns: List[Any]
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/template/cloudx/manage/apps",
                    return_type=List[Any],
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return add_apps_(self._request_adapter)
