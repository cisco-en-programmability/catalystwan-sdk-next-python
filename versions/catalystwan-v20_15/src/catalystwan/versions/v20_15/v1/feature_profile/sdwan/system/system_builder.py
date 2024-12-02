# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .aaa.aaa_builder import AaaBuilder
    from .banner.banner_builder import BannerBuilder
    from .basic.basic_builder import BasicBuilder
    from .bfd.bfd_builder import BfdBuilder
    from .global_.global_builder import GlobalBuilder
    from .logging.logging_builder import LoggingBuilder
    from .mrf.mrf_builder import MrfBuilder
    from .ntp.ntp_builder import NtpBuilder
    from .omp.omp_builder import OmpBuilder
    from .snmp.snmp_builder import SnmpBuilder
    from .security.security_builder import SecurityBuilder


class SystemBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/system
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdwan_system_feature_profiles(
        self, offset: Optional[int] = None, limit: Optional[int] = 0, **kw
    ) -> Any:
        """
        Get all SDWAN Feature Profiles with giving Family and profile type

        :param offset: Pagination offset
        :param limit: Pagination limit
        :returns: Any
        """
        params = {
            "offset": offset,
            "limit": limit,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/v1/feature-profile/sdwan/system", params=params, **kw
        )

    @property
    def create_sdwan_system_feature_profile(self):
        class create_sdwan_system_feature_profile_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[str] = None, **kw) -> str:
                """
                Create a SDWAN System Feature Profile

                :param payload: SDWAN Feature profile
                :returns: str
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/system",
                    return_type=str,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return create_sdwan_system_feature_profile_(self._request_adapter)

    def get_sdwan_system_feature_profile_by_profile_id(
        self, system_id: str, **kw
    ) -> Any:
        """
        Get a SDWAN System Feature Profile with systemId

        :param system_id: Feature Profile Id
        :returns: Any
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/system/{systemId}",
            params=params,
            **kw,
        )

    @property
    def edit_sdwan_system_feature_profile(self):
        class edit_sdwan_system_feature_profile_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, system_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Edit a SDWAN System Feature Profile

                :param system_id: Feature Profile Id
                :param payload: SDWAN Feature profile
                :returns: str
                """
                params = {
                    "systemId": system_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/system/{systemId}",
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

        return edit_sdwan_system_feature_profile_(self._request_adapter)

    def delete_sdwan_system_feature_profile(self, system_id: str, **kw):
        """
        Delete Feature Profile

        :param system_id: System id
        :returns: None
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/system/{systemId}",
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
    def basic(self) -> BasicBuilder:
        """
        The basic property
        """
        from .basic.basic_builder import BasicBuilder

        return BasicBuilder(self._request_adapter)

    @property
    def bfd(self) -> BfdBuilder:
        """
        The bfd property
        """
        from .bfd.bfd_builder import BfdBuilder

        return BfdBuilder(self._request_adapter)

    @property
    def global_(self) -> GlobalBuilder:
        """
        The global property
        """
        from .global_.global_builder import GlobalBuilder

        return GlobalBuilder(self._request_adapter)

    @property
    def logging(self) -> LoggingBuilder:
        """
        The logging property
        """
        from .logging.logging_builder import LoggingBuilder

        return LoggingBuilder(self._request_adapter)

    @property
    def mrf(self) -> MrfBuilder:
        """
        The mrf property
        """
        from .mrf.mrf_builder import MrfBuilder

        return MrfBuilder(self._request_adapter)

    @property
    def ntp(self) -> NtpBuilder:
        """
        The ntp property
        """
        from .ntp.ntp_builder import NtpBuilder

        return NtpBuilder(self._request_adapter)

    @property
    def omp(self) -> OmpBuilder:
        """
        The omp property
        """
        from .omp.omp_builder import OmpBuilder

        return OmpBuilder(self._request_adapter)

    @property
    def security(self) -> SecurityBuilder:
        """
        The security property
        """
        from .security.security_builder import SecurityBuilder

        return SecurityBuilder(self._request_adapter)

    @property
    def snmp(self) -> SnmpBuilder:
        """
        The snmp property
        """
        from .snmp.snmp_builder import SnmpBuilder

        return SnmpBuilder(self._request_adapter)
