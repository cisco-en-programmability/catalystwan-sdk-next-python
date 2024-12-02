# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .bifrost_controller_registration.bifrost_controller_registration_builder import \
        BifrostControllerRegistrationBuilder
    from .cci.cci_builder import CciBuilder
    from .enroll.enroll_builder import EnrollBuilder
    from .get_bi_frost_signing_key.get_bi_frost_signing_key_builder import GetBiFrostSigningKeyBuilder
    from .get_controller_client_token.get_controller_client_token_builder import GetControllerClientTokenBuilder
    from .profiles.profiles_builder import ProfilesBuilder
    from .registration.registration_builder import RegistrationBuilder


class DashboardBuilder:
    """
    Builds and executes requests for operations under /dashboard
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def bifrost_controller_registration(self) -> BifrostControllerRegistrationBuilder:
        """
        The bifrostControllerRegistration property
        """
        from .bifrost_controller_registration.bifrost_controller_registration_builder import \
            BifrostControllerRegistrationBuilder

        return BifrostControllerRegistrationBuilder(self._request_adapter)

    @property
    def cci(self) -> CciBuilder:
        """
        The cci property
        """
        from .cci.cci_builder import CciBuilder

        return CciBuilder(self._request_adapter)

    @property
    def enroll(self) -> EnrollBuilder:
        """
        The enroll property
        """
        from .enroll.enroll_builder import EnrollBuilder

        return EnrollBuilder(self._request_adapter)

    @property
    def get_bi_frost_signing_key(self) -> GetBiFrostSigningKeyBuilder:
        """
        The getBiFrostSigningKey property
        """
        from .get_bi_frost_signing_key.get_bi_frost_signing_key_builder import GetBiFrostSigningKeyBuilder

        return GetBiFrostSigningKeyBuilder(self._request_adapter)

    @property
    def get_controller_client_token(self) -> GetControllerClientTokenBuilder:
        """
        The getControllerClientToken property
        """
        from .get_controller_client_token.get_controller_client_token_builder import GetControllerClientTokenBuilder

        return GetControllerClientTokenBuilder(self._request_adapter)

    @property
    def profiles(self) -> ProfilesBuilder:
        """
        The profiles property
        """
        from .profiles.profiles_builder import ProfilesBuilder

        return ProfilesBuilder(self._request_adapter)

    @property
    def registration(self) -> RegistrationBuilder:
        """
        The registration property
        """
        from .registration.registration_builder import RegistrationBuilder

        return RegistrationBuilder(self._request_adapter)
