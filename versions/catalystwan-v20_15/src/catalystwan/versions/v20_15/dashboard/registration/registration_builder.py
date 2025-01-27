# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .status.status_builder import StatusBuilder


class RegistrationBuilder:
    """
    Builds and executes requests for operations under /dashboard/registration
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def registration(self, payload: Optional[Any] = None, **kw):
        """
        Register Controller to BiFrost Dashboard (by Controller)

        :param payload: CD profile to be registered
        :returns: None
        """
        return self._request_adapter.request(
            "POST", "/dataservice/dashboard/registration", payload=payload, **kw
        )

    def deregistration(self, deregister_by_force: Optional[bool] = False, **kw):
        """
        De-registration Controller (by Controller)

        :param deregister_by_force: deregister by force
        :returns: None
        """
        params = {
            "deregisterByForce": deregister_by_force,
        }
        return self._request_adapter.request(
            "DELETE", "/dataservice/dashboard/registration", params=params, **kw
        )

    @property
    def status(self) -> StatusBuilder:
        """
        The status property
        """
        from .status.status_builder import StatusBuilder

        return StatusBuilder(self._request_adapter)
