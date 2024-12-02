# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .properties.properties_builder import PropertiesBuilder


class QueueBuilder:
    """
    Builds and executes requests for operations under /statistics/on-demand/queue
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_queue_entries(self, **kw) -> Any:
        """
        gets current on-demand queue entries

        :returns: Any
        """
        return self._request_adapter.request(
            "GET", "/dataservice/statistics/on-demand/queue", **kw
        )

    @property
    def create_queue_entry(self):
        class create_queue_entry_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Create on-demand troubleshooting queue entry

                :param payload: On-demand queue entry
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/statistics/on-demand/queue",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return create_queue_entry_(self._request_adapter)

    @property
    def update_queue_entry(self):
        class update_queue_entry_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, entry_id: str, payload: Optional[Any] = None, **kw
            ) -> Any:
                """
                Updates on-demand troubleshooting queue entry

                :param entry_id: Entry Id
                :param payload: On-demand queue entry
                :returns: Any
                """
                params = {
                    "entryId": entry_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/statistics/on-demand/queue/{entryId}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return update_queue_entry_(self._request_adapter)

    def delete_queue_entry(self, entry_id: str, **kw):
        """
        removes on-demand queue entry

        :param entry_id: Entry Id
        :returns: None
        """
        params = {
            "entryId": entry_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/statistics/on-demand/queue/{entryId}",
            params=params,
            **kw,
        )

    @property
    def properties(self) -> PropertiesBuilder:
        """
        The properties property
        """
        from .properties.properties_builder import PropertiesBuilder

        return PropertiesBuilder(self._request_adapter)
