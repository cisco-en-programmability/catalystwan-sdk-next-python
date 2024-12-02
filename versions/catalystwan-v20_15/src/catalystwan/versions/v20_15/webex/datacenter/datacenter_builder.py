# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import WebexDataCenter

if TYPE_CHECKING:
    from .sync.sync_builder import SyncBuilder
    from .syncstatus.syncstatus_builder import SyncstatusBuilder


class DatacenterBuilder:
    """
    Builds and executes requests for operations under /webex/datacenter
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def get_webex_data_centers(self):
        class get_webex_data_centers_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[WebexDataCenter] = None, **kw) -> bool:
                """
                TEMP-Insert webex data center details manually for test setup

                :param payload: Webex Data Center
                :returns: bool
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/webex/datacenter",
                    return_type=bool,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> WebexDataCenter:
                return WebexDataCenter(*args, **kwargs)

            @property
            def payload_model(self) -> Type[WebexDataCenter]:
                return WebexDataCenter

        return get_webex_data_centers_(self._request_adapter)

    def delete_webex_data_centers(self, **kw) -> bool:
        """
        Delete webex data center data in DB

        :returns: bool
        """
        return self._request_adapter.request(
            "DELETE", "/dataservice/webex/datacenter", return_type=bool, **kw
        )

    @property
    def sync(self) -> SyncBuilder:
        """
        The sync property
        """
        from .sync.sync_builder import SyncBuilder

        return SyncBuilder(self._request_adapter)

    @property
    def syncstatus(self) -> SyncstatusBuilder:
        """
        The syncstatus property
        """
        from .syncstatus.syncstatus_builder import SyncstatusBuilder

        return SyncstatusBuilder(self._request_adapter)
