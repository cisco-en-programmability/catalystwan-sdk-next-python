# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import ProtocolPackUpgradeRequest

if TYPE_CHECKING:
    from .cancel.cancel_builder import CancelBuilder
    from .status.status_builder import StatusBuilder


class UpgradeBuilder:
    """
    Builds and executes requests for operations under /sdavc/protocol-pack/maintenance/upgrade
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def upgrade_protocol_pack(self):
        class upgrade_protocol_pack_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[ProtocolPackUpgradeRequest] = None, **kw
            ):
                """
                Deploy protocol pack to devices

                :param payload: Request Payload
                :returns: None
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/sdavc/protocol-pack/maintenance/upgrade",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> ProtocolPackUpgradeRequest:
                return ProtocolPackUpgradeRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[ProtocolPackUpgradeRequest]:
                return ProtocolPackUpgradeRequest

        return upgrade_protocol_pack_(self._request_adapter)

    @property
    def cancel(self) -> CancelBuilder:
        """
        The cancel property
        """
        from .cancel.cancel_builder import CancelBuilder

        return CancelBuilder(self._request_adapter)

    @property
    def status(self) -> StatusBuilder:
        """
        The status property
        """
        from .status.status_builder import StatusBuilder

        return StatusBuilder(self._request_adapter)
