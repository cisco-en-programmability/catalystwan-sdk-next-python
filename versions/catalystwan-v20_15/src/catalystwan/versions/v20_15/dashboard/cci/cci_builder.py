# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .authorize.authorize_builder import AuthorizeBuilder
    from .token.token_builder import TokenBuilder


class CciBuilder:
    """
    Builds and executes requests for operations under /dashboard/cci
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def authorize(self) -> AuthorizeBuilder:
        """
        The authorize property
        """
        from .authorize.authorize_builder import AuthorizeBuilder

        return AuthorizeBuilder(self._request_adapter)

    @property
    def token(self) -> TokenBuilder:
        """
        The token property
        """
        from .token.token_builder import TokenBuilder

        return TokenBuilder(self._request_adapter)
