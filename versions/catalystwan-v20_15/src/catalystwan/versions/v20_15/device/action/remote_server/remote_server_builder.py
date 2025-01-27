# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import Any, Optional

from catalystwan.abc import RequestAdapterInterface


class RemoteServerBuilder:
    """
    Builds and executes requests for operations under /device/action/remote-server
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_remote_server_list(self, **kw) -> Any:
        """
        Get list of remote servers

        :returns: Any
        """
        return self._request_adapter.request(
            "GET", "/dataservice/device/action/remote-server", **kw
        )

    def add_remote_server(self, payload: Optional[Any] = None, **kw):
        """
        Add a new remote server entry.

        :param payload: Request body for Add a new remote server entry.
        :returns: None
        """
        return self._request_adapter.request(
            "POST", "/dataservice/device/action/remote-server", payload=payload, **kw
        )

    def get_remote_server_by_id(self, id: str, **kw) -> Any:
        """
        Get remote server for the specified ID

        :param id: Id
        :returns: Any
        """
        params = {
            "id": id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/device/action/remote-server/{id}", params=params, **kw
        )

    def update_remote_server(self, id: str, payload: Optional[str] = None, **kw) -> Any:
        """
        Update remote server for the specified ID

        :param id: Id
        :param payload: Payload
        :returns: Any
        """
        params = {
            "id": id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/device/action/remote-server/{id}",
            params=params,
            payload=payload,
            **kw,
        )

    def delete_remote_server(self, id: str, payload: Optional[Any] = None, **kw):
        """
        Delete remote server for the specified ID

        :param id: remoteServerId
        :param payload: Request body for Add a new remote server entry.
        :returns: None
        """
        params = {
            "id": id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/device/action/remote-server/{id}",
            params=params,
            payload=payload,
            **kw,
        )
