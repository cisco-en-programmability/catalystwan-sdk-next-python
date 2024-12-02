# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .aaa.aaa_builder import AaaBuilder
    from .banner.banner_builder import BannerBuilder
    from .logging.logging_builder import LoggingBuilder
    from .ntp.ntp_builder import NtpBuilder
    from .snmp.snmp_builder import SnmpBuilder
    from .system_settings.system_settings_builder import SystemSettingsBuilder


class SystemBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/nfvirtual/system
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_all_nfvirtual_system_feature_profiles(
        self, offset: Optional[int] = None, limit: Optional[int] = 0, **kw
    ) -> Any:
        """
        Get all Nfvirtual System Feature Profiles

        :param offset: Pagination offset
        :param limit: Pagination limit
        :returns: Any
        """
        params = {
            "offset": offset,
            "limit": limit,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/nfvirtual/system",
            params=params,
            **kw,
        )

    @property
    def create_nfvirtual_system_feature_profile(self):
        class create_nfvirtual_system_feature_profile_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[str] = None, **kw) -> str:
                """
                Create a nfvirtual System Feature Profile

                :param payload: Nfvirtual Feature profile
                :returns: str
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/nfvirtual/system",
                    return_type=str,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return create_nfvirtual_system_feature_profile_(self._request_adapter)

    def get_nfvirtual_system_feature_profile_by_profile_id(
        self, system_id: str, **kw
    ) -> Any:
        """
        Get a Nfvirtual System Feature Profile with systemId

        :param system_id: Feature Profile Id
        :returns: Any
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/nfvirtual/system/{systemId}",
            params=params,
            **kw,
        )

    @property
    def edit_nfvirtual_system_feature_profile(self):
        class edit_nfvirtual_system_feature_profile_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, system_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Edit a Nfvirtual System Feature Profile

                :param system_id: Feature Profile Id
                :param payload: Nfvirtual Feature profile
                :returns: str
                """
                params = {
                    "systemId": system_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/nfvirtual/system/{systemId}",
                    return_type=str,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return edit_nfvirtual_system_feature_profile_(self._request_adapter)

    def delete_nfvirtual_system_feature_profile(self, system_id: str, **kw):
        """
        Delete a Nfvirtual System Feature Profile

        :param system_id: Feature Profile Id
        :returns: None
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/nfvirtual/system/{systemId}",
            params=params,
            **kw,
        )

    @property
    def aaa(self) -> AaaBuilder:
        """
        The aaa property
        """
        from .aaa.aaa_builder import AaaBuilder

        return AaaBuilder(self._request_adapter)

    @property
    def banner(self) -> BannerBuilder:
        """
        The banner property
        """
        from .banner.banner_builder import BannerBuilder

        return BannerBuilder(self._request_adapter)

    @property
    def logging(self) -> LoggingBuilder:
        """
        The logging property
        """
        from .logging.logging_builder import LoggingBuilder

        return LoggingBuilder(self._request_adapter)

    @property
    def ntp(self) -> NtpBuilder:
        """
        The ntp property
        """
        from .ntp.ntp_builder import NtpBuilder

        return NtpBuilder(self._request_adapter)

    @property
    def snmp(self) -> SnmpBuilder:
        """
        The snmp property
        """
        from .snmp.snmp_builder import SnmpBuilder

        return SnmpBuilder(self._request_adapter)

    @property
    def system_settings(self) -> SystemSettingsBuilder:
        """
        The system-settings property
        """
        from .system_settings.system_settings_builder import SystemSettingsBuilder

        return SystemSettingsBuilder(self._request_adapter)
