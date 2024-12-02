# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, List, Optional

from catalystwan.abc import RequestAdapterInterface


class CustomappBuilder:
    """
    Builds and executes requests for operations under /template/policy/customapp
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_custom_apps(self, **kw) -> List[Any]:
        """
        Get all policy custom applications

        :returns: List[Any]
        """
        return self._request_adapter.request(
            "GET", "/dataservice/template/policy/customapp", return_type=List[Any], **kw
        )

    def create_custom_app(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Create a policy custom applications

        :param payload: App payload
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/template/policy/customapp", payload=payload, **kw
        )

    def get_custom_app_by_id(self, id: str, **kw) -> Any:
        """
        Get a policy custom applications

        :param id: Id
        :returns: Any
        """
        params = {
            "id": id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/template/policy/customapp/{id}", params=params, **kw
        )

    def edit_custom_app(self, id: str, payload: Optional[Any] = None, **kw):
        """
        Edit a policy custom applications

        :param id: Id
        :param payload: App payload
        :returns: None
        """
        params = {
            "id": id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/template/policy/customapp/{id}",
            params=params,
            payload=payload,
            **kw,
        )

    def delete_custom_app(self, id: str, **kw):
        """
        Delete a policy custom applications

        :param id: Id
        :returns: None
        """
        params = {
            "id": id,
        }
        return self._request_adapter.request(
            "DELETE", "/dataservice/template/policy/customapp/{id}", params=params, **kw
        )
